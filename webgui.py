from flask import Flask , request , send_from_directory , render_template
from flask import *
import time
import requests
import json
import random
from tqdm import tqdm
from threading import Thread
class webgui:
    msgs = []
def startWeb():
    url = 'http://localhost:81/postComment'
    #Loading config
    f = open("config.json", "r")
    jason = json.loads(f.read())
    f.close()
    debugon = "false"
    ops = jason["ops"]
    ignored = jason["banned"]
    usrname = jason["username"]
    accID = jason["accountid"]
    passwrd = jason["password"]
    levelID = jason["levelID"]
    debugon = jason["debug"]
    def log(text):
        print(text)
        file = open("programlogs.txt", "a")
        file.write("\n" + text)
        file.close()
    def silentlog(text):
        file = open("programlogs.txt", "a")
        file.write("\n" + text)
        file.close()
    def say(text):
        global lastsaid
        try:
            x = requests.post(url, data={"username":usrname,"accountID":accID,"password":passwrd,"levelID":levelID,"percent":"0","comment":text})
            log("[LOG] Successfully sent the following text: " + text)
        except:
            log("[ERR] Error while trying to send the following text: " + text)
        lastsaid = text
    app = Flask(__name__)



    @app.route('/static/<path:path>')
    def statics(path):
        return send_from_directory('static', path)

    @app.route('/favicon.ico')
    def favs():
        return send_from_directory('static', 'favicon.ico')

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/login")
    def login():
        e="Username or password incorrect"
        username = request.args.get("name")
        password = request.args.get("pass")
        if username == usrname and password == passwrd:
            return render_template("loggedin.html", usr = username, passw = password)
        else:
            return e

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html", usr = usrname)

    @app.route("/livefeed")
    def lifefeed():
        if len(webgui.msgs) > 9:
            while len(webgui.msgs) > 9:
                webgui.msgs.pop(0)
        feedtext = ""
        for msg in webgui.msgs:
            feedtext = feedtext + "<br>"+msg
        return render_template("livefeed.html", feed = feedtext)

    @app.route("/check")
    def check():
        e="false"
        string = request.args.get("to")
        username = string.split(";")[0]
        password = string.split(";")[1]
        if username == usrname and password == passwrd:
            e = "true"
        return e

    @app.route("/sendmsg")
    def sendmsg():
        string = request.args.get("to")
        messg = request.args.get("msg")
        username = string.split(";")[0]
        password = string.split(";")[1]
        if username == usrname and password == passwrd:
            say(messg)
            return "1"
        else:
            return "0"

    @app.route("/splitusr")
    def splitpassw():
        string = request.args.get("to")
        usr = string.split(";")[0]
        return usr

    @app.route("/splitpass")
    def splitusr():
        string = request.args.get("to")
        passw = string.split(";")[1]
        return passw

    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory('static', '404.html')

    @app.errorhandler(500)
    def erroronserver(e):
        return send_from_directory('static', '500.html')
    log("[Web] Loaded")

    app.run(port=80,host="0.0.0.0")
t = Thread(target=startWeb)
t.start()