#! python3
import pyautogui
import schedule
import time

name = input('Enter your name : ')

def msg():
    global name
    pyautogui.click(x=546,y=695)
    pyautogui.typewrite([list(name),' ','p','r','e','s','e','n','t','enter'],interval=0.1)

def test():
    pyautogui.click(x=49, y=44)
    time.sleep(10)
    pyautogui.click(x=1201, y=79, clicks = 2)
    time.sleep(2)
    pyautogui.click(x=1164, y=710, clicks = 2)
    pyautogui.typewrite([list(name),' ','enter'],interval=0.1)


schedule.every().day.at("07:30").do(msg)

while True:
    schedule.run_pending()
    print('trying to run')
    time.sleep(10)
