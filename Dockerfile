FROM python:3.11-slim

# Set work directory
WORKDIR /src

# Copiamos el archivos de requerimientos
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Copiar código de aplicación
COPY src .