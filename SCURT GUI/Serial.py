import serial
import time

ser = serial.Serial("COM12",9600,timeout=3)
def command ():
    x = input("enter your command : ").encode('ascii')

    time.sleep(3)
    info = ser.write(x)
    print(info)

    return command()
if __name__ == '__main__': command()

