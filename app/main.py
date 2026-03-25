from flask import Flask, jsonify
import platform
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/health')
def health():
    logger.info('Health check requested')
    return jsonify({'status': 'ok'})

@app.route('/api/info')
def info():
    logger.info('Info endpoint requested')
    return jsonify({
        'hostname': platform.node(),
        'python_version': platform.python_version(),
        'environment': os.getenv('ENVIRONMENT', 'local'),
        'message': 'DevOps Platform funcionando'
    })

@app.route('/api/stress')
def stress():
    result = sum(i * i for i in range(100000))
    logger.warning(f'Stress test: {result}')
    return jsonify({'result': result})
