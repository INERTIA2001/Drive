import login as ls

name = ls.pyautogui.prompt("what is your name?")
nameBot = ls.pyautogui.prompt("what will be your bot name?\nthis should be simple!!")
usr = ls.pyautogui.confirm("are you sure")
if usr == "CANCEL":
    pass
elif usr == "OK":
    user = ls.BOT(name = name,nameBot = nameBot,standby=True)
    user.onCreate()
d = ls.shelve.open('myfile.db')
d['data'] = user
d.close() 