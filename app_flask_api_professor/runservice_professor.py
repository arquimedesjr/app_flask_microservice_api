from flask import Flask, render_template
from professores_api import professores_app
import requests as Req
import infra.professores_db as professores_db


app = Flask(__name__)
app.register_blueprint(professores_app)

@app.route('/')
def professor():
    professores = Req.get("http://localhost:5001/professores").json()
    return render_template("index.html", professores=professores)

professores_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
