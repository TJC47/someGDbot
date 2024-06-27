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
gomenu = False
ecr = False
def log(text):
    print(text)
    file = open("programlogs.txt", "a")
    file.write("\n" + text)
    file.close()
def silentlog(text):
    file = open("programlogs.txt", "a")
    file.write("\n" + text)
    file.close()
def inputl(text):
    out = input(text)
    silentlog(text+out)
    return out
def uwuwifie(text):
    return text.lower().replace("uwu","[120120113]").replace("l","w").replace("i","iw").replace("a","aw").replace("e","ew").replace("u","uw").replace("o","ow").replace("y","yw").replace("s","w").replace("[120120113]","UwU")
log("[LOG] Configurated ")
def debugmsg(text):
    log(f"[Debug] {text}")
if debugon.lower() == "true":
    debugmsg("Debug mode enabled. Press ctrl + c for more options.")
def debug():
    global debugon
    global gomenu
    debugshon = True
    silentlog("[Debug] type 'return' to return to normal program function 'help' for help.")
    print("\n[Debug] type 'return' to return to normal program function 'help' for help.")
    while debugshon:
        try:
            debugsh = inputl("[Debug] $ ").lower()
            if debugsh == "return":
                debugshon = False
            elif debugsh == "help":
                debugmsg("return, menu, debug")
            elif debugsh == "menu":
                debugmsg("Going to menu!")
                gomenu = True
                debugshon = False
            elif debugsh == "debug":
                inp = inputl("[Debug] Turn debug mode on/off > ").lower()
                if inp == "on":
                    debugon = "true"
                elif inp == "off":
                    debugon = "false"
                else:
                    debugmsg("Not a valid option! exiting function!")
        except:
            print("")
            debugshon = False

while botgui.running:
    try:
        log("[LOG] Connecting...")
        ids = []
        url = 'http://localhost:81/postComment'
        def say(text):
            global lastsaid
            try:
                x = requests.post(url, data={"username":usrname,"accountID":accID,"password":passwrd,"levelID":levelID,"percent":"0","comment":text})
                log("[LOG] Successfully sent the following text: " + text)
            except:
                log("[ERR] Error while trying to send the following text: " + text)
            lastsaid = text
        url = 'http://localhost:81/postComment'
        while botgui.running:
            if gomenu:
                raise Exception("Menu")
            ecr = True
            comments=requests.get("http://localhost:81/api/comments/"+levelID+"?count="+str(commentfetch)) # annoying issue, please dont make this very high.
            comments=json.loads((comments.text))
            jason["banned"] = ignored
            jason["ops"] = ops
            fi = open("config.json","w")
            fi.write(str(jason).replace("'",'"'))
            fi.close()
            ecr = False
            for comment in range(0,commentfetch): #adjust this or it will crash
                comment1=dict(comments[comment])["content"]
                comment2=dict(comments[comment])
                #Debug testing
                if debugon.lower() == "true":
                    try:
                        comment1 = inputl("[Debug] Message > ")
                        comment2 = {}
                        comment2["ID"] = random.randint(1,100000)
                        comment2["username"] = "CONSOLE"
                    except:
                        debug()
                        comment1 = ""
                        comment2 = {}
                        comment2["ID"] = random.randint(1,100000)
                        comment2["username"] = "[DontLog]"
                if not comment2["ID"] in ids:
                    if not comment2["username"].lower() in ignored and not comment2["username"] == "[DontLog]":
                        ids.append(comment2["ID"])
                        print(comment2["username"]+": "+comment1)
                        file = open("log.txt", "a")
                        file.write("\n"+comment2["username"]+": "+comment1)
                        file.close()
                        arguments = comment1.split(' ', 1)
                        icnf = False
                        if comment1.lower().startswith("/help") and not comment2["username"]==usrname:
                            if comment2["username"].lower() in ops:
                                say("@"+comment2["username"]+" OPCommands: /furry /ai /cool /yesorno /say /op /deop /oplist /pen_s /banlist /ban /unban /stats /help /UwU /dice")
                                icnf = True
                            else:
                                say("@"+comment2["username"]+" Commands: /furry /ai /cool /yesorno /say /oplist /banlist /stats /help /UwU /dice")
                                icnf = True
                        if comment2["username"].lower() in ops and not comment2["username"]==usrname:
                            if comment1.lower().startswith("/op "):
                                say("["+comment2["username"]+" opped "+comment1.split(' ', 1)[1].replace("@", "")+"]")
                                ops.append(comment1.split(' ', 1)[1].lower().replace("@", ""))
                                icnf = True
                            if comment1.lower().startswith("/ban "):
                                say("Banned "+"@"+comment1.split(' ', 1)[1].replace("@", ""))
                                ignored.append(comment1.split(' ', 1)[1].lower().replace("@", ""))
                                icnf = True
                            if comment1.lower().startswith("/deop "):
                                say("["+comment2["username"]+" deopped "+comment1.split(' ', 1)[1].replace("@", "")+"]")
                                ops.remove(comment1.split(' ', 1)[1].lower().replace("@", ""))
                                icnf = True
                            if comment1.lower().startswith("/unban "):
                                say("Unbanned "+"@"+comment1.split(' ', 1)[1].replace("@", ""))
                                ignored.remove(comment1.split(' ', 1)[1].lower().replace("@", ""))
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
                        elif comment1.lower().startswith("/dice") and not comment2["username"]==usrname:
                            try:
                                if len(comment1.split(' ', 1)) > 1:
                                    sides = int(comment1.split(' ', 1)[1])
                                else:
                                    sides = 6
                                say("@"+comment2["username"]+" you rolled a "+str(random.randint(1,sides))+" on the "+str(sides)+" sided dice!")
                            except:
                                say("@"+comment2["username"]+" you must use a whole number(no decimals) as an argument!")
                        elif comment1.lower().startswith("/yesorno") and not comment2["username"]==usrname:
                            if "rac" in comment1.lower():
                                say("@"+comment2["username"]+" No, im not racist. Racism should be illegal!")
                            else:
                                random.seed(comment1.lower())
                                say("@"+comment2["username"]+" "+random.choice(["yes","no"]))
                                random.seed()
                        elif comment1.lower().startswith("/ai") and not comment2["username"]==usrname:
                            if len(comment1.split(' ', 1)) > 1:
                                resp = requests.get("http://api.brainshop.ai/get?bid=172425&key=f1KfI93QOBQaqZQb&uid=someone&msg="+comment1.split(' ', 1)[1], headers={'Accept': 'application/json'})
                                jsonResp = json.loads(resp.text)
                                response = jsonResp["cnt"]
                            else:
                                response = "Please include a message to ask the AI. Usage: /ai <message>"
                            say("@"+comment2["username"]+" "+response)
                        elif comment1.lower().startswith("/say") and not comment2["username"]==usrname:
                            if len(comment1.split(' ', 1)) > 1:
                                say(f"@{comment2["username"]} {comment1.split(' ', 1)[1]}")
                            else:
                                say(f"@{comment2["username"]} Please include a message to say. Usage: /say <message>")
                        elif comment1.lower().startswith("/uwu") and not comment2["username"]==usrname:
                            if len(comment1.split(' ', 1)) > 1:
                                say(f"@{comment2["username"]} {uwuwifie(comment1.split(' ', 1)[1])}")
                            else:
                                say(f"@{comment2["username"]} pwewawwew iwncwuwdew aw mewwwawgew tow mawkew UwU. uwwawgew: /UwU <mewwwawgew>")
                        elif comment1.lower().startswith("/stats") and not comment2["username"]==usrname:
                            stats = json.loads(requests.get("http://localhost:81/api/profile/" + comment2["username"]).text)
                            say("@"+comment2["username"]+ f"  has {stats['stars']} stars, {stats['diamonds']} diamonds, {stats['coins']} coins, {stats['userCoins']} user coins, {stats['demons']} demons beaten and {stats['cp']} creator points.")
                        elif comment1.lower().startswith("/oplist") and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" OPS:"+str(ops))
                        #elif "hello" in comment1.lower() and not comment2["username"]==usrname:
                            #say("@"+comment2["username"]+" Hello!")
                        elif "skibidi" in comment1.lower() and not comment2["username"]==usrname:
                            say("Banned "+"@"+comment2["username"])
                            ignored.append(comment2["username"].lower())
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
            if gomenu:
                gomenu = False
                raise Exception("Menu")
            if ecr:
                log("Could not connect to servers. Trying again in 5 seconds. Are you running GDColons GDBrowser on port 81?")
            else:
                log("Press Ctrl + C in 5 seconds for menu")
            time.sleep(5)
        except:
            sel = inputl("[Menu] 'exit' to exit, 'shell' for debug shell > ").lower()
            if sel == "exit":
                break
            elif sel == "shell":
                debug()
            else:
                log("[Menu] Invalid selection! Returning!")
            log("[Debug] Returned!")
botgui.running = False
log("[LOG] Saving New Config...")
try:
    fi = open("config.json","w")
    fi.write(str(jason).replace("'",'"'))
    fi.close()
    log("[LOG] Success!")
except:
    log("[ERR] Failed saving config!")
