from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Inicio"

@app.route("/home")
def home():
    return "Home"

@app.route("/ingreso/<id>")
def ingreso(id):
    return f"Ingreso {id}"