#! python3
import pyautogui
import schedule
import time

def msg():
    pyautogui.click(x=546,y=695)
    pyautogui.typewrite(['S','a','i',' ','S','a','b','a','r','i','s','h',' ','p','r','e','s','e','n','t',' ','m','a',"'",'a','m','enter'],interval=0.1)

def test():
    pyautogui.click(x=49, y=44)
    time.sleep(10)
    pyautogui.click(x=1201, y=79, clicks = 2)
    time.sleep(2)
    pyautogui.click(x=1164, y=710, clicks = 2)
    pyautogui.typewrite(['S','a','i',' ','S','a','b','a','r','i','s','h',' ','1','2','H','2','6','enter'],interval=0.1)


schedule.every().day.at("07:30").do(msg)

while True:
    schedule.run_pending()
    print('trying to run')
    time.sleep(10)
