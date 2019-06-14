import pygame
from pygame import locals
import serial
import time

ser=serial.Serial("COM6",9600)

pygame.init()       #inciiar pygame
pygame.joystick.init()      #iniciar lib joystick    
print ("se detecto: "),pygame.joystick.get_count()," joystick" #cuantos joystick estan conectados

j0=pygame.joystick.Joystick(0)  #seleccionamos el joystick a utilizar
j0.init()   #inicializar el j0

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
                    if(posx == 1):
                        print ("right")
                        ser.write(b'e')
                    elif(posx < -1):
                        print ("LEFT")
                        ser.write(b'f')
                            
                elif (axis == "Y"):
                    posy = e.dict['value']
                    if(posy < -1):
                        print ("up")
                        ser.write(b'r')
                    elif(posy == 1):
                        print ("down")
                        ser.write(b'l')




        if e.type == pygame.locals.JOYBUTTONDOWN:
            if e.dict['button']==0:
                print ("arriba")
                ser.write(b'a')
                #time.sleep(0.1)
            elif e.dict['button']==1:
                print ("derecha")
                ser.write(b's')
                #time.sleep(0.1)
            elif e.dict['button']==2:
                print ("abajo")
                ser.write(b'r')
                #time.sleep(0.1)
            elif e.dict['button']==3:
                print ("izquierda")
        elif e.type == pygame.locals.JOYBUTTONUP:
            print ("deje de presionar")
            ser.write(b's')
