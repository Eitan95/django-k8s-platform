# Builder Stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Instalación a nivel de sistema dentro del builder
RUN pip install --no-cache-dir -r requirements.txt

# Final Stage
FROM python:3.12-slim
WORKDIR /app

# Copiar las librerías instaladas en el sistema
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

# Crear usuario y asignar permisos
RUN useradd -m appuser && chown -R appuser:appuser /app

USER appuser

# Colectar estáticos
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
