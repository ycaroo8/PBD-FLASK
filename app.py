from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá</h1> <h2>Mundo!</h2>"

@app.route("/aluno/<nome>")
def aluno(nome):
    return nome