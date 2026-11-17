from flask import Flask 
import random



app = Flask(__name__)

@app.route("/")
def test():
    return """
    <html>
        <head>
            <link rel="stylesheet" href="static/style.css">
        </head>
        <body>
            <a href="/randompass">
                <button>password generator</button>
            </a>
            <a href="/headsortails">
                <button>Head or Tails</button>
            </a>
            <img src="static/image/image.jpg">
        </body>
    </html>
    """
@app.route("/randompass")
def randompass():
    caratteri = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm.,-_@!$/=1234567890"
    password = ""
    for i in range(15):
        password += random.choice(caratteri)
    return f"<p>{password}</p>"
@app.route("/headsortails")
def headortails():
    headtails = random.choice("head","tails")
    return f"<p>{headtails}</p>"



app.run(debug=True)