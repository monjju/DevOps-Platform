from flask import Flask, jsonify
import platform
import os
import logging
import time
import random

# OpenTelemetry imports
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource

# Prometheus exporter
from prometheus_flask_exporter import PrometheusMetrics

# Configurar recurso
resource = Resource.create({
    "service.name": "devops-platform",
    "service.version": "3.0",
    "deployment.environment": os.getenv("ENVIRONMENT", "dev")
})

# Configurar Tracer
tracer_provider = TracerProvider(resource=resource)
otlp_trace_exporter = OTLPSpanExporter(
    endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector-opentelemetry-collector:4317"),
    insecure=True
)
tracer_provider.add_span_processor(BatchSpanProcessor(otlp_trace_exporter))
trace.set_tracer_provider(tracer_provider)

# Configurar Meter
metric_reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(
        endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector-opentelemetry-collector:4317"),
        insecure=True
    ),
    export_interval_millis=5000
)
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)

# Crear tracer y meter
tracer = trace.get_tracer("devops-platform")
meter = metrics.get_meter("devops-platform")

# Métricas custom OTel
request_counter = meter.create_counter(
    "app_requests_total",
    description="Total requests por endpoint"
)
latency_histogram = meter.create_histogram(
    "app_request_duration_ms",
    description="Latencia de requests en ms"
)

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Instrumentar Flask con OTel
FlaskInstrumentor().instrument_app(app)

# Añadir Prometheus exporter — expone /metrics
prometheus_metrics = PrometheusMetrics(app)
prometheus_metrics.info('app_info', 'Application info', version='3.0', environment=os.getenv('ENVIRONMENT', 'dev'))

@app.route('/health')
def health():
    request_counter.add(1, {"endpoint": "/health"})
    return jsonify({'status': 'ok', 'version': '3.0'})

@app.route('/api/info')
def info():
    start = time.time()
    with tracer.start_as_current_span("get-system-info") as span:
        span.set_attribute("hostname", platform.node())
        span.set_attribute("environment", os.getenv("ENVIRONMENT", "dev"))

        request_counter.add(1, {"endpoint": "/api/info"})
        logger.info(f"Info requested - trace_id: {span.get_span_context().trace_id}")

        duration = (time.time() - start) * 1000
        latency_histogram.record(duration, {"endpoint": "/api/info"})

        return jsonify({
            'hostname': platform.node(),
            'python_version': platform.python_version(),
            'environment': os.getenv('ENVIRONMENT', 'dev'),
            'message': 'DevOps Platform v3.0 - OTel + Prometheus instrumented'
        })

@app.route('/api/stress')
def stress():
    start = time.time()
    with tracer.start_as_current_span("stress-test") as span:
        sleep_time = random.uniform(0.1, 0.5)
        time.sleep(sleep_time)

        result = sum(i * i for i in range(100000))
        span.set_attribute("result", result)
        span.set_attribute("sleep_time_ms", sleep_time * 1000)

        request_counter.add(1, {"endpoint": "/api/stress"})
        duration = (time.time() - start) * 1000
        latency_histogram.record(duration, {"endpoint": "/api/stress"})

        logger.warning(f"Stress test completed in {duration:.2f}ms")
        return jsonify({'result': result, 'duration_ms': round(duration, 2)})

@app.route('/api/error')
def simulate_error():
    with tracer.start_as_current_span("simulate-error") as span:
        request_counter.add(1, {"endpoint": "/api/error"})
        if random.random() < 0.5:
            span.set_attribute("error", True)
            span.record_exception(Exception("Simulated error for SLO testing"))
            logger.error("Simulated error triggered")
            return jsonify({'error': 'Simulated error'}), 500
        return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
