from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    tiempo = datetime.now()
    formato = tiempo.strftime("%Y-%m-%d %I:%M:%S %p")
    message = "¡Bienvenido a mi aplicación web en Python!"
    return f"<h1>{message}</h1><p>Fecha y hora actuales: {formato}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
