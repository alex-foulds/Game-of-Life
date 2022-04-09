from xml.etree.ElementInclude import include
from flask import Flask, render_template
from gridFunctions import *

app = Flask(__name__)

@app.route("/")
def mainPage():
    createGraph()
    #return "<h1>This is the Mainpage</h1> Hello <h2>Testing</h2>
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(use_reloader=True)