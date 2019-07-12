import login as l

d = l.shelve.open('myfile.db')
user = d['data']
d.close()

user.greet()
while True:
    while user.standby == True:
        comm = user.listen()
        if comm == user.nameBot:
            user.exitstandby()
            break
        elif "close" in comm:
            l.sys.exit()
    while user.standby == False:
        comm = user.listen()
        if "rest" in comm:
            user.standby()
            break
        elif "write" in comm:
            user.writingMode()
        elif "open" in comm:
            user.openApplication()