# Builder Stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final Stage
FROM python:3.12-slim
WORKDIR /app

# Copiar dependencias del builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

# Crear usuario y otorgar permisos sobre /app antes de cambiar de usuario
RUN useradd -m appuser && chown -R appuser:appuser /app

USER appuser

# Colectar estáticos (ahora appuser sí tiene permisos de escritura en /app)
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]