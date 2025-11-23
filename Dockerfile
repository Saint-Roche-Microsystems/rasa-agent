FROM rasa/rasa

# Cambiar temporalmente a root
USER root

# Instalar spacy y el modelo
RUN pip install --no-cache-dir spacy && \
    python -m spacy download es_core_news_md

# Restaurar usuario por defecto de Rasa (1001)
USER 1001

# Copiar el proyecto
COPY . /app
WORKDIR /app
