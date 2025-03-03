# Usa l'immagine ufficiale Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt .
COPY app.py .
COPY ai_operator.py .

# Crea le directory necessarie
RUN mkdir -p templates static/css static/js

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta su cui l'app ascolterà
ENV PORT 8080
EXPOSE 8080

# Avvia l'applicazione
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
