import os
import socket
from flask import Flask

VERSION = "v1"  # en el ejercicio 2 lo cambiarás a "v2"
app = Flask(__name__)

@app.route("/")
def hola():
    mensaje = os.environ.get("MENSAJE", "Hola desde un contenedor")
    return f"{mensaje} | version {VERSION} | host {socket.gethostname()}\n"
