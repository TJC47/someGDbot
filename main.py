import botgui
import requests
import time
import json
import random
from threading import Thread
ignored =[]
icnf = False
ops = ["tjc472"]
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
commentfetch = 3
debugon = jason["debug"]
ids = []
alreadyrun = False
lastsaid = ""

print("Configurated ")
def debugmsg(text):
    print(f"[Debug] {text}")
if debugon.lower() == "true":
    debugmsg("Debug mode enabled. Press ctrl + c for more options.")
def debug():
    global debugon
    debugshon = True
    print("\n[Debug] type 'return' to return to normal program function 'help' for help.")
    while debugshon:
        debugsh = input("[Debug] $ ").lower()
        if debugsh == "return":
            debugshon = False
        elif debugsh == "help":
            debugmsg("return, debug")
        elif debugsh == "debug":
            inp = input("[Debug] Turn debug mode on/off > ").lower()
            if inp == "on":
                debugon = "true"
            elif inp == "off":
                debugon = "false"
            else:
                debugmsg("Not a valid option! exiting function!")
while botgui.running:
    try:
        print("Connecting...")
        ids = []
        url = 'http://localhost/postComment'
        def say(text):
            global lastsaid
            x = requests.post(url, data={"username":usrname,"accountID":accID,"password":passwrd,"levelID":levelID,"percent":"0","comment":text})
            print(text)
            lastsaid = text
        url = 'http://localhost/postComment'
        while botgui.running:
            comments=requests.get("http://localhost/api/comments/"+levelID+"?count="+str(commentfetch)) # annoying issue, please dont make this very high.
            comments=json.loads((comments.text))
            jason["banned"] = ignored
            jason["ops"] = ops
            fi = open("config.json","w")
            fi.write(str(jason).replace("'",'"'))
            fi.close()
            for comment in range(0,commentfetch): #adjust this or it will crash
                comment1=dict(comments[comment])["content"]
                comment2=dict(comments[comment])
                #Debug testing
                if debugon.lower() == "true":
                    try:
                        comment1 = input("[Debug] Message > ")
                        comment2["ID"] = random.randint(1,100000)
                        comment2["username"] = "CONSOLE"
                    except:
                        debug()
                if not comment2["ID"] in ids:
                    if not comment2["username"].lower() in ignored:
                        ids.append(comment2["ID"])
                        print(comment2["username"]+": "+comment1)
                        file = open("log.txt", "a")
                        file.write("\n"+comment2["username"]+": "+comment1)
                        file.close()
                        arguments = comment1.split(' ', 1)
                        icnf = False
                        if comment1.lower().startswith("/help") and not comment2["username"]==usrname:
                            if comment2["username"].lower() in ops:
                                say("@"+comment2["username"]+" OPCommands: /furry /ai /cool /yesorno /say /op /oplist /pen_s /banlist /ban /stats /help")
                                icnf = True
                            else:
                                say("@"+comment2["username"]+" Commands: /furry /ai /cool /yesorno /say /oplist /banlist /stats /help")
                                icnf = True
                        if comment2["username"].lower() in ops and not comment2["username"]==usrname:
                            if comment1.lower().startswith("/op "):
                                say("["+comment2["username"]+" opped "+comment1.split(' ', 1)[1]+"]")
                                ops.append(comment1.split(' ', 1)[1].lower())
                                icnf = True
                            if comment1.lower().startswith("/ban "):
                                say("Banned "+"@"+comment1.split(' ', 1)[1])
                                ignored.append(comment1.split(' ', 1)[1].lower())
                                icnf = True
                            if comment1.lower().startswith("/pen_s") and not comment2["username"]==usrname:
                                say("@"+comment2["username"]+" B==D")
                                icnf = True
                        if comment1.lower().startswith("/furry") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" you are "+str(random.randint(0,100))+"% a furry.")
                        elif comment1.lower().startswith("/banlist") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" BANNED:"+str(ignored))
                        elif comment1.lower().startswith("/cool") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" you are "+str(random.randint(0,100))+"% cool.")
                        elif comment1.lower().startswith("/yesorno") and not comment2["username"]==usrname:
                            random.seed(comment1.lower())
                            say("@"+comment2["username"]+" "+random.choice(["yes","no"]))
                            random.seed()
                        elif comment1.lower().startswith("/ai") and not comment2["username"]==usrname:
                            resp = requests.get("http://api.brainshop.ai/get?bid=172425&key=f1KfI93QOBQaqZQb&uid=someone&msg="+comment1.split(' ', 1)[1], headers={'Accept': 'application/json'})
                            jsonResp = json.loads(resp.text)
                            response = jsonResp["cnt"]
                            say("@"+comment2["username"]+" "+response)
                        elif comment1.lower().startswith("/say") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" "+comment1.split(' ', 1)[1])
                        elif comment1.lower().startswith("/stats") and not comment2["username"]==usrname:
                            stats = json.loads(requests.get("http://localhost/api/profile/" + comment2["username"]).text)
                            say("@"+comment2["username"]+ f"  has {stats['stars']} stars, {stats['diamonds']} diamonds, {stats['coins']} coins, {stats['userCoins']} user coins, {stats['demons']} demons beaten and {stats['cp']} creator points.")
                        elif comment1.lower().startswith("/oplist") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" OPS:"+str(ops))
                        elif "hello" in comment1.lower() and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" Hello!")
                        elif comment1.startswith("/") and not icnf and not comment2["username"]==usrname:
                            if comment2["username"].lower() in ops:
                                say("@"+comment2["username"]+" you have op but this command doesn't exist /help for a list of commands")
                            else:
                                say("@"+comment2["username"]+" im sorry but you don't have op /help for a list of commands") #avoids spamming chat if possible making a cooldown for this message (see todo list) would be the right way 
                        botgui.comment = comment2["username"]+ ": " + comment1
                        botgui.lastsaid = lastsaid
                        #if alreadyrun == False:
                        #    alreadyrun = True
                        #    guiwin=Thread(target=botgui.start)
                        #    guiwin.start()
            if not debugon.lower() ==  "true":
                time.sleep(2) # Make the bot check every 2 seconds instead, You shouldnt be ratelimited.
    except:
        try:
            print("Press Ctrl + C in 5 seconds for menu")
            time.sleep(5)
        except:
            sel = input("[Menu] 'exit' to exit, 'shell' for debug shell > ").lower()
            if sel == "exit":
                break
            elif sel == "shell":
                debug()
            else:
                print("[Menu] Invalid selection! Returning!")
botgui.running = False
print("Saving New Config...")
try:
    fi = open("config.json","w")
    fi.write(str(jason).replace("'",'"'))
    fi.close()
    print("Success!")
except:
    print("Failed!")
