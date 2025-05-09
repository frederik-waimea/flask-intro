from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.get("/test")
def test ():
    return "<h1>Testing ....1...2....3</h1>"



