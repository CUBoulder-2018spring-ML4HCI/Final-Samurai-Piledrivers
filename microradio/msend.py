from microbit import *
import radio

radio.on()

radio.config(channel=16)
radio.config(power=7)

while True:
        acc_x=str(accelerometer.get_x())
        acc_y=accelerometer.get_y()
        acc_z=accelerometer.get_z()
        if acc_x is not None & acc_y is not None & acc_z is not None:
        radio.send(str(acc_x) + ", " + str(acc_y) + ", " + str(acc_z) + ", ")
