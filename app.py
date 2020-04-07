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
    with open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'r') as f:
        content = f.read()
    return render_template('home.html', content=content)

@app.route("/Users")
def addUser():
    with open(r"C:\Users\Derek\PycharmProjects\webapp\Users.txt", 'r') as f:
        content = f.read()
    return render_template('users.html', content=content)


@app.route('/Remove', methods=['GET','POST'])
def removeUser():
    message = ""
    if request.method == 'POST':
        result = request.form['nameRemove']
        completion = removeSavedImage.main(result)

        if completion == 1:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write(
                "[%s] User: %s Has been Removed \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            print("Updated Log")
            path = '..'
            os.chdir(path)
            with open(r"C:\Users\Derek\PycharmProjects\webapp\Users.txt", 'r') as f:
                lines = f.readlines()
            with open(r"C:\Users\Derek\PycharmProjects\webapp\Users.txt", 'w') as f:
                for line in lines:
                    if line.strip("\n") != result:
                        f.write(line)
            print("Updated Users")
            message = "Success! user '%s' has been removed" % result
        elif completion == 0:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write(
                "[%s] Unable to remove. User: %s does not exist \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            print("Updated Log")
            print("Updated Log")
            path = '..'
            os.chdir(path)
            message = " Unable to remove user. User '%s' does not exist" % result

        else:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write(
                "[%s] Unknown remove request for %s, please try again later \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            print("Updated Log")
            path = '..'
            os.chdir(path)
            message = "Error: Please try again"

    return render_template('removeUser.html', message = message)

@app.route('/Add', methods=['GET','POST'])
def add():
    message = ""
    if request.method =='POST':
        result = request.form['name']
        print("User Added: ", result)
        completion = saveUserImage.main(result)

        if completion == 1:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write("[%s] User: %s Has been Created \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            print("Updated Log")

            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Users.txt", 'a')
            f.write("%s\n" % result)
            f.close()
            print("Updated Users")
            message = "Success! user '%s' has been added" % result
        elif completion == 0:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write(
                "[%s] Failed to add User: %s exists already \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            print("Updated Log")
            message = " Unable to add user. User '%s' already exists" % result
        else:
            f = open(r"C:\Users\Derek\PycharmProjects\webapp\Logs.txt", 'a')
            f.write(
                "[%s] Unknown add request for  %s, please try again later \n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result))
            f.close()
            message = "Error: Please try again"

    return render_template('add.html', message = message)

if __name__ == '__main__':
    app.run()
