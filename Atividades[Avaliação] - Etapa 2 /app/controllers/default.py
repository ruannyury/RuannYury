from app import app, db
from flask import render_template
from app.models.tables import User

# from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(username="ruannyury").first()
    r.name = "Ruann Y."
    db.session.add(r)
    db.session.commit()
    print(r.name)
    return "Ok."
