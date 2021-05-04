#! python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
import pyautogui
import schedule
import time

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.initUI()

    name = input('Enter name : ')

    def attendWhatsapp(self):
        def msg():
	    global name
            pyautogui.click(x=546,y=695)
            pyautogui.typewrite([list(name),'enter'],interval=0.1)
        schedule.every().day.at("07:30").do(test)
        while True:
            schedule.run_pending()
            print('trying to run')
            time.sleep(10)

    def initUI(self):
	    self.setGeometry(200, 200, 300, 300)
	    self.setWindowTitle("AutoAttendance")

	    self.label = QtWidgets.QLabel(self)
	    self.label.setText("Whaddaya Need To Attend?")
	    self.label.move(50,50)

	    self.b1 = QtWidgets.QPushButton(self)
	    self.b1.setText("Whatsapp!")
	    self.b1.clicked.connect(self.attendWhatsapp)

def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

main()

'''
def Window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle('Python Application')

    label = QLabel(win)
    label.setText('H3ll0 TH3R3')
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

Window()
'''
