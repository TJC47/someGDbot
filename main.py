print("Starting")
import requests
import time
import json
import random
print("Loaded libraries!")
ignored =["autoworks","fursona"]
ops = ["tjc472"]
bannedwords= ["deez nuts","bi*ch","b*tch","ban me","s*x","im a furry","uwu","balls","sex","sus","nya"]
f = open("config.json", "r")
jason = json.loads(f.read())
f.close()
ops = jason["ops"]
ignored = jason["banned"]
usrname = jason["username"]
accID = jason["accountid"]
passwrd = jason["password"]
levelID = jason["levelID"]
ids = []
print("Loaded CONFIG!")
while True:
    try:
        print("Trying to Connect")
        ids = []
        url = 'http://localhost/postComment'
        def say(text):
            x = requests.post(url, data={"username":usrname,"accountID":accID,"password":passwrd,"levelID":levelID,"percent":"0","comment":text})
            print(text)
        url = 'http://localhost/postComment'
        while True:
            comments=requests.get("http://localhost/api/comments/"+levelID+"?count=11")
            comments=json.loads((comments.text))
            jason["banned"] = ignored
            jason["ops"] = ops
            fi = open("config.json","w")
            fi.write(str(jason).replace("'",'"'))
            fi.close()
            for comment in range(0,10):
                comment1=dict(comments[comment])["content"]
                comment2=dict(comments[comment])
                #print(comment1)
                if not comment2["ID"] in ids:
                    if not comment2["username"].lower() in ignored:
                        ids.append(comment2["ID"])
                        print(comment2["username"]+": "+comment1)
                        file = open("log.txt", "a")
                        file.write("\n"+comment2["username"]+": "+comment1)
                        file.close()
                        if "/help" in comment1.lower() and not comment2["username"]==usrname:
                            if comment2["username"].lower in ops:
                                say("@"+comment2["username"]+" OPCommands: /furry /cool /yesorno /say /op /oplist /pen_s /banlist /ban /help")
                            else:
                                say("@"+comment2["username"]+" Commands: /furry /cool /yesorno /say /oplist /banlist /help")
                            print("command /help")
                        if comment2["username"].lower() in ops and not comment2["username"]==usrname:
                            if "/op" in comment1:
                                say("["+comment2["username"]+" opped"+comment1.split(' ', 1)[1]+"]")
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
                            say("@"+comment2["username"]+" "+random.choice(["yes","no","ha","totally not randimized","stop spamming!","what da","uwu","owo"]))
                        elif "/say" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" "+comment1.split(' ', 1)[1])
                        elif "/oplist" in comment1 and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" OPS:"+str(ops))
                        elif "gg" in comment1.lower() and not comment2["username"]==usrname:
                            say("@"+comment2["username"]+" Good Game!")
                        elif "/" in comment1 and not comment2["username"]==usrname:
                            if comment2["username"].lower in ops:
                                say("@"+comment2["username"]+" you have op but this command doesn't exist /help for a list of commands")
                            else:
                                say("@"+comment2["username"]+" im sorry but you don't have op /help for a list of commands")
                        for bw in bannedwords:
                            if bw in comment1.lower() and not comment2["username"]=="TJC472":
                                say("@"+comment2["username"]+" You have been banned from TJC472's bot. Reason: '"+comment1+"' /banlist!!!")
                                ignored.append(comment2["username"].lower())
            time.sleep(5)
    except:
        pass
