FROM python:3.11-slim

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup main.py .

USER appuser

EXPOSE 8080

CMD ["python", "-m", "flask", "--app", "main", "run", "--host=0.0.0.0", "--port=8080"]
