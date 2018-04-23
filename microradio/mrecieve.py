from microbit import *
import radio

radio.on()
radio.config(channel=16)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strength


# Event loop.
while True:
        incoming = str(radio.receive())
        print(incoming)
        sleep(200)
