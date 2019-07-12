import pyautogui 
import sys
from random import randint
import pyttsx3
import time
import speech_recognition as sr
import shelve
import os
import subprocess

class BOT:
    def __init__(self,name,nameBot,standby=True):
        General.__init__(self)
        Mouse.__init__(self)
        Keyboard.__init__(self)
        self.name = name
        self.nameBot = nameBot
        self.standby = standby
        print("the bot is created")
    def onCreate(self):
        General.say("Hello {}, I am {}, and I will help you".format(self.name,self.nameBot))
        General.say("you can run main.py now....")
        General.say("Thank you....")
    def greet(self):
        General.say("welcome back {}".format(self.name))
        General.say("{} is ready to help you, just say the word".format(self.nameBot))
    def standby(self):
        General.say("standing by")
        self.standby = True
    def exitstandby(self):
        General.say("how can I help You?")
        self.standby = False
    def close(self):
        General.say("Thank you, I shall shut down...")
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("speak...")
            audio = r.listen(source)
            try:
                print("listening...")
                comm = r.recognize_google(audio)
                return str(comm)
            except:
                if self.standby == True:
                    pass
                elif self.standby == False:
                    General.say("please try again")
    def openApplication(self):
        target = self.listen()
        target = str(target).capitalize()
        Keyboard.boot(target)
    def writingMode(self):
        while True:
            General.say("initiating writing mode...")
            read = ""
            General.say("you mau begin...")
            string=self.listen()
            read += string
            if string.lower() == "stop":
                General.say("exiting writing mode...")
                break
            elif string == "read":
                General.say(read)
            elif string == "enter":
                Keyboard.press("enter")
            else:
                Keyboard.write(string)
    def tutorial(self):
        General.say("Hello, today I will tell you how I work!")
        General.say("There are a lot of functions I can do, but I will explain what I am intended to do")
        General.say("but for now I have 2 modes, ready to be used")
        General.say("Writing mode...")
        General.say("please say what you want to write...")
        General.say("if you want to exit writing mode, say 'stop'")
        General.say("if you want to write in a new line, say 'enter'")
        General.say("Booting mode....")
        General.say("you can boot your applications here")
        General.say("just make sure to speak clearly...")
        General.say("That is all for today, please stay tuned for more!")
    def Credits(self):
        General.say("Thank you for using me!")
        General.say("I am a companion bot designed to help you!")
        print("Thank you!")
        General.say("I am created by my author, William")
        print("personal Info:\ne-mail : williamgozali2001@gmail.com")
        General.say("yu can contact him for your support, complain or even Idea!")
        

class Keyboard:
    def __init__(self):
        print("keyboard override")
    def copy():
        pyautogui.hotkey("command","c")
    def paste():
        pyautogui.hotkey("command","v")
    def undo():
        pyautogui.hotkey("command","z")
    def screen():
        pyautogui.hotkey("command","shift","3")
    def save():
        pyautogui.hotkey("command","s")
    def boot(target):
        os.system(f"open /Application/{target}.app")
    def write(string):
        pyautogui.typewrite(string)
    def press(target):
        pyautogui.press(target)
    def navigate():
        pyautogui.keyDown("command","tab")

class Mouse:
    def __init__(self):
        print('mouse initiated')
    def scrollUp():
        pyautogui.scroll(10)
    def scrolldown():
        pyautogui.scroll(-10)
    def click():
        pyautogui.doubleClick()

class General:
    def __init__(self):
        print("adhering general functions...")
    def say(string):
        print(string)
        engine = pyttsx3.init()
        engine.say(string)
        engine.runAndWait()
    def reply(string):
        print(string)
        say(string)
    def wait(num):
        time.sleep(num)
    def comment():
        num = randint(1,3)
        if num == 1:
            reply("Hey, I am a bot not a smart guy")
        elif num == 2:
            reply("please say something I understand")
        elif num == 3:
            reply("Would it hurt to say something I understand?")
