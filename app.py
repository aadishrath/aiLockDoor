from flask import Flask, render_template, url_for, send_from_directory
from time import sleep

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/User")
def addUser():
    return render_template('addUser.html')

@app.route('/logs')
def logs():
   with open("Logs.txt", "r") as f:
       content = f,read()
       return render_template('home.html', content=content)


if __name__ == '__main__':
    app.run()
