from flask import Flask, render_template
from disciplinas_api import disciplinas_app
import requests as Req
import infra.disciplina_db as disciplinas_db

app = Flask(__name__)
app.register_blueprint(disciplinas_app)

@app.route('/')
def disciplinas():
    disciplinas = Req.get("http://localhost:5003/disciplinas").json()
    return render_template("index.html", disciplina=disciplinas)

disciplinas_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=5003)
