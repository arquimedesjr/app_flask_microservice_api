from flask import Flask, render_template
from alunos_api import alunos_app

import requests as Req
import infra.alunos_db as alunos_db

app = Flask(__name__)
app.register_blueprint(alunos_app)

@app.route('/')
def alunos():
    alunos = Req.get("http://localhost:5000/alunos").json()
    return render_template("index.html", alunos=alunos)

alunos_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
