from flask import Flask

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "<h1>This is the Mainpage</h1> Hello <h2>Testing</h2>"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)