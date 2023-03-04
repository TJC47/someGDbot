import requests
import time
import json
import random

ignored =[]
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
while True:
    try:
        print("Connecting...")
        ids = []
        url = 'http://localhost/postComment'
        def say(text):
            x = requests.post(url, data={"username":usrname,"accountID":accID,"password":passwrd,"levelID":levelID,"percent":"0","comment":text})
            print(text)
        url = 'http://localhost/postComment'
        while True:
            comments=requests.get("http://localhost/api/comments/"+levelID+"?count=3") # annoying issue, please dont make this very high.
            comments=json.loads((comments.text))
            jason["banned"] = ignored
            jason["ops"] = ops
            fi = open("config.json","w")
            fi.write(str(jason).replace("'",'"'))
            fi.close()
            for comment in range(0,3): #adjust this or it will crash
                comment1=dict(comments[comment])["content"]
                comment2=dict(comments[comment])
                #Debug testing
                if debugon.lower() == "true":
                    try:
                        comment1 = input("[Debug] Message > ")
                        comment2["ID"] = random.randint(1,100000)
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
                        if "/help" in comment1.lower() and not comment2["username"]==usrname:
                            if comment2["username"].lower in ops:
                                say("@"+comment2["username"]+" OPCommands: /furry /ai /cool /yesorno /say /op /oplist /pen_s /banlist /ban /stats /help")
                            else:
                                say("@"+comment2["username"]+" Commands: /furry /ai /cool /yesorno /say /oplist /banlist /stats /help")
                            print("command /help")
                        if comment2["username"].lower() in ops and not comment2["username"]==usrname:
                            if "/op" in comment1:
                                say("["+comment2["username"]+" opped "+comment1.split(' ', 1)[1]+"]")
                                ops.append(comment1.split(' ', 1)[1].lower())
                            if "/ban" in comment1:
                                say("Banned "+"@"+comment1.split(' ', 1)[1])
                                ignored.append(comment1.split(' ', 1)[1].lower())
                            if "/pen_s" in comment1 and not comment2["username"]==usrname:
                                say("@"+comment2["username"]+" B==D")
                        elif "/furry" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" you are "+str(random.randint(0,100))+"% a furry.")
                        elif "/banlist" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" BANNED:"+str(ignored))
                        elif "/cool" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" you are "+str(random.randint(0,100))+"% cool.")
                        elif "/yesorno" in comment1.lower() and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" "+random.choice(["yes","no"]))
                        elif "/ai" in comment1 and not comment2["username"]==usrname:
                            resp = requests.get("http://api.brainshop.ai/get?bid=172425&key=f1KfI93QOBQaqZQb&uid=0&msg="+comment1.split(' ', 1)[1], headers={'Accept': 'application/json'})
                            jsonResp = json.loads(resp.text)
                            response = jsonResp["cnt"]
                            say("@"+comment2["username"]+" "+response)
                        elif "/say" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" "+comment1.split(' ', 1)[1])
                        elif "/stats" in comment1 and not comment2["username"]==usrname:
                            stats = json.loads(requests.get("http://localhost/api/profile/" + comment2["username"]).text)
                            say("@"+comment2["username"]+ f"  has {stats['stars']} stars, {stats['diamonds']} diamonds, {stats['coins']} coins, {stats['userCoins']} user coins, {stats['demons']} demons beaten and {stats['cp']} creator points.")
                        elif "/oplist" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" OPS:"+str(ops))
                        elif "gg" in comment1.lower() and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" Good Game!")
                        elif "/" in comment1 and not comment2["username"]==usrname:
                            if comment2["username"].lower in ops:
                                say("@"+comment2["username"]+" you have op but this command doesn't exist /help for a list of commands")
                            else:
                                pass#say("@"+comment2["username"]+" im sorry but you don't have op /help for a list of commands") avoids spamming chat if possible making a cooldown for this message (see todo list) would be the right way 
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
