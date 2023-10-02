FROM python:3.10

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

# Añadir Flask 2.0.1, una versión compatible con Werkzeug
RUN pip install Flask==2.0.1

EXPOSE 5000

CMD ["python3", "app.py"]

