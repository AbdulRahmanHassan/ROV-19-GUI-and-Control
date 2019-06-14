from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
#______________________________________
import pygame
from pygame import locals
#_______________________________________

import ROV_rc
import time
import os
from os import path
import sys

import threading


import serial


ser = serial.Serial("COM16",115200)

time.sleep(1)

FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"main.ui"))



class MainApp(QMainWindow , FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)



        '''
        
                            if e.dict['button'] == 9:
                        ser.write(b'a')
        self.A_button()
        self.B_button()
        self.up_button()
        self.down_button()
        self.right_button()
        self.left_button()
        self.rt_button()
        self.stop_button()
'''
        self.pushButton_8.clicked.connect(self.A_button)
        self.pushButton.clicked.connect(self.up_button)
        self.pushButton_3.clicked.connect(self.down_button)
        self.pushButton_5.clicked.connect(self.right_button)
        self.pushButton_4.clicked.connect(self.left_button)
        self.pushButton_9.clicked.connect(self.rt_button)
        self.pushButton_11.clicked.connect(self.stop_button)
        self.pushButton_7.clicked.connect(self.B_button)




    ###########Buttons############

    def A_button (self):
        info = ser.write(b'w')         #Go Forward
        print("Forward")
        self.textBrowser.append("Rov Is Going Forward.")

    def B_button (self):
        info = ser.write(b's')
        print("Backward")
        self.textBrowser.append("Rov Is Going Backward.")

    def up_button (self):
        info = ser.write(b'e')
        print("Up")
        self.textBrowser.append("Rov Is Going Up.")

    def down_button (self):
        info = ser.write(b'q')
        print("Down")
        self.textBrowser.append("Rov Is Going Down.")

    def right_button (self):
        info = ser.write(b'd')
        print("Right")
        self.textBrowser.append("Rov Is Going Right.")

    def left_button (self):
        info = ser.write(b'a')
        print("Left")
        self.textBrowser.append("Rov Is Going Left.")


    def rt_button (self):
        info = ser.write(b'r')
        print("Rotate")
        self.textBrowser.append("Rov Is Rotated.")

    def stop_button (self):
        info = ser.write(b'f')
        print("Stop")
        self.textBrowser.append("Rov Is Stoped.")

'''    pygame.init()  # inciiar pygame
    pygame.joystick.init()  # iniciar lib joystick
    print("se detecto: "), pygame.joystick.get_count(), " joystick"  # cuantos joystick estan conectados

    j0 = pygame.joystick.Joystick(0)  # seleccionamos el joystick a utilizar
    j0.init()  # inicializar el j0

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.locals.JOYBUTTONDOWN:
                if e.dict['button'] == 0:
                    ser.write(b's')
                elif e.dict['button'] == 1:
                    ser.write(b'w')
                    # time.sleep(0.1)
                elif e.dict['button'] == 2:
                    ser.write(b'd')
                    # time.sleep(0.1)
                elif e.dict['button'] == 3:
                    ser.write(b'a')


                elif e.type == pygame.locals.JOYBUTTONUP:
                    print("deje de presionar")
                    ser.write(b'f')

'''



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()         #infint loop


if __name__ == '__main__':
    main()

def joysticks():
    pygame.init()  # intialiate pygame
    pygame.joystick.init()  # intialiate joystick
    print("Conected: ", pygame.joystick.get_count(),"joysticks" )  # how many joystick are connected
    j0 = pygame.joystick.Joystick(1)  # we select the joystick to use
    j0.init()  # inicializar el j0


    while 1:
        for e in pygame.event.get():

            if e.type == pygame.JOYAXISMOTION:
                axis = "unknown"
                if (e.dict['axis'] == 0):
                    axis = "X"

                if (e.dict['axis'] == 1):
                    axis = "Y"

                if (e.dict['axis'] == 2):
                    axis = "Throttle"

                if (e.dict['axis'] == 3):
                    axis = "Z"

                if (axis != "unknown"):
                    str = "Axis: %s; Value: %f" % (axis, e.dict['value'])
                    if (axis == "X"):
                        posx = e.dict['value']
                        if (posx == 1):
                            print("right")
                            ser.write(b'd')
                        elif (posx < -1):
                            print("LEFT")
                            ser.write(b'a')

                    elif (axis == "Y"):
                        posy = e.dict['value']
                        if (posy < -1):
                            print("Forward")
                            ser.write(b'w')
                        elif (posy == 1):
                            print("Backword")
                            ser.write(b's')

            if e.type == pygame.locals.JOYBUTTONDOWN:
                if e.dict['button'] == 0:
                    ser.write(b'q')
                    print("Forward")
                elif e.dict['button'] == 1:
                    ser.write(b'd')
                    print("Right")
                    # time.sleep(0.1)
                elif e.dict['button'] == 2:
                    ser.write(b'e')
                    print("Backward")
                    # time.sleep(0.1)
                elif e.dict['button'] == 3:
                    ser.write(b'a')
                    print("Left")

                elif e.dict['button'] == 7:
                    ser.write(b'x')
                    print("ARM Open")
                elif e.dict['button'] == 5:
                    ser.write(b'y')
                    print("ARM Close")

                elif e.dict['button'] == 11:
                    ser.write(b'r')
                    print("Rotate")

                elif e.dict['button'] == 4:
                    ser.write(b'x')
                    print("arm close")

                elif e.dict['button'] == 6:
                    ser.write(b'y')
                    print("arm open")

                elif e.dict['button'] == 10:
                    ser.write(b'f')
                    print("Stop")

#                elif e.dict['button'] == 13:
 #                   ser.write(b'f')
  #                  print("Stop")

t1 = threading.Thread(target=joysticks, args=())
t2 = threading.Thread(target=main, args=())

t1.start()
t2.start()

t1.join()
t2.join()

#_______________________________________


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
