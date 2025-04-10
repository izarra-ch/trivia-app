FROM python:3.11-slim

# Creamos directorio de la app
WORKDIR /app

# Copiamos el archivos de requerimientos
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

RUN pwd

RUN ls

# Copiar código de aplicación
COPY ./src ./src

# Ejecutamos nuestra app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]