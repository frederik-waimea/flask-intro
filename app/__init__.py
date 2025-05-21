from flask import Flask
from flask import render_template
from supabase import create_client
from dotenv import load_dotenv
import os
app = Flask(__name__)
#Get Environemt variables
load_dotenv()
SUPABASE_URL= os.getenv("SUPABASE_URL")
SUPABASE_KEY= os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL,SUPABASE_KEY)

app = Flask(__name__)

@app.get("/")
def home():
    response =supabase.table("things").select().order("name").execute()
    records = response.data
    return render_template("pages/home.jinja", things=records)

@app.get("/test/")
def test ():
    return render_template ("<h1>Testing ....1...2....3</h1>")

@app.get ("/about/")
def about ():
    return render_template ("tree")

@app.get ("/random/")
def random():
    randNum = randint (1, 1000)
    return render_template("pages/random.jinja"); number = randNum

@app.get("/thing/<int:id>")
def showThing(id):
     response =supabase.table("things").select().eq("id", id).single().order("name").execute()
     record = response.data
     
     return render_template("pages/home.jinja", thing=record)
@app.get("/thing/<int:id>")
def deleteThing(id):
    # TODO!!!!!

    return 
@app.errorhandler(404)
def notFound(error):
    return render_template ("pages/404.jinja")



