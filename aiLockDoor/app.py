from flask import Flask, render_template, url_for, send_from_directory, request
from time import sleep
import datetime
import saveUserImage
import removeSavedImage
import os
import csv

app = Flask(__name__)


@app.route('/')
def home():
    with open(r"bin/logs.txt", 'r') as f:
        content = f.read()
    return render_template('home.html', content=content)


@app.route("/Users")
def addUser():
    with open(r"bin/users.txt", 'r') as f:
        content = f.read()
    return render_template('users.html', content=content)


@app.route('/Remove', methods=['GET', 'POST'])
def removeUser():
    if request.method == 'POST':
        result = request.form['nameRemove']
        removeSavedImage.main(result)
        os.chdir('..')
        f = open(r"bin/logs.txt", 'a')
        f.write("[%s] User: %s Has been Removed \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
        f.close()
        print("Updated Log")
        with open(r"bin/users.txt", 'r') as f:
            lines = f.readlines()
        with open(r"bin/users.txt", 'w') as f:
            for line in lines:
                if line.strip("\n") != result:
                    f.write(line)
        print("Updated Users")
    return render_template('removeUser.html')


@app.route('/Add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        result = request.form['name']
        print("User Added: ", result)
        saveUserImage.main(result)
        f = open(r"bin/logs.txt", 'a')
        f.write("[%s] User: %s Has been Created \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
        f.close()
        print("Updated Log")

        f = open(r"bin/users.txt", 'a')
        f.write("%s\n" % result)
        f.close()
        print("Updated Users")

    return render_template('add.html')


if __name__ == '__main__':
    app.run()
