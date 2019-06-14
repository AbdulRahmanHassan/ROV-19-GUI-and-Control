from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import ROV_rc
import time
import os
from os import path

import sys

import serial


ser = serial.Serial("COM11",9600)

time.sleep(1)

FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))


class MainApp(QMainWindow , FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.A_button()
        self.B_button()
        self.up_button()
        self.down_button()
        self.right_button()
        self.left_button()
        self.rt_button()
        self.stop_button()


    ###########Buttons############

    def A_button (self):
        self.pushButton_8.clicked.connect(self.A_button)
        info = ser.write(b'w')
        print(info)
        return (self)

    def B_button (self):
        self.pushButton_7.clicked.connect(self.B_button)
        info = ser.write(b's')
        print(info)
        #return self.B_button

    def up_button (self):
        self.pushButton.clicked.connect(self.up_button)
        info = ser.write(b'e')
        print(info)

    def down_button (self):
        self.pushButton_3.clicked.connect(self.down_button)
        info = ser.write(b'q')
        print(info)


    def right_button (self):
        self.pushButton_5.clicked.connect(self.right_button)
        info = ser.write(b'd')
        print(info)


    def left_button (self):
        self.pushButton_4.clicked.connect(self.left_button)
        info = ser.write(b'a')
        print(info)


    def rt_button (self):
        self.pushButton_9.clicked.connect(self.rt_button)
        info = ser.write(b'r')
        print(info)


    def stop_button (self):
        self.pushButton_11.clicked.connect(self.stop_button)
        info = ser.write(b'f')
        print(info)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__== '__main__':
    main()



'''class App:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Frannie")

        # Set up the joystick
        pygame.joystick.init()

        self.clock = pygame.time.Clock()

        self.serReadCount = 0
        self.amps = 0
        self.distLog = []
        self.graphPoints = []

        self.my_joystick = None
        self.joystick_names = []

       '''
