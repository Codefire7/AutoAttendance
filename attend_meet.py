import webbrowser
import pyautogui
import time

name = input('Enter name : ')

def login(sub):
    profile = "Profile 5"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --profile-directory="{}" %s'.format(profile)
    webbrowser.get(chrome_path).open(sub_url(sub))
    post_join()

def sub_url(sub):
    if sub.lower() in ['chem','che','chemistry']:
        return 'https://meet.google.com/<id>'
    elif sub.lower() in ['phy','physics']:
        return 'https://meet.google.com/<id>'
    elif sub.lower() in ['math','maths']:
        return 'https://meet.google.com/<id>'
    elif sub.lower() in ['cs','csc']:
        return 'https://meet.google.com/<id>'
    elif sub.lower() in ['eng','english']:
        return 'https://meet.google.com/<id>'
    elif sub.lower() in ['test']:
        return 'https://meet.google.com/ndi-efnv-cxb'

def post_join():
    global name
    time.sleep(10)
    pyautogui.click(x=1201, y=79, clicks = 2)
    time.sleep(2)
    pyautogui.click(x=1164, y=710, clicks = 2)
    pyautogui.typewrite([list(name),'enter'],interval=0.1)

def main():
    sub = input('Enter subject:')
    login(sub)
