import RPi.GPIO as GPIO
import time
import random
import numpy as np
import signal
import sys


# setup the mode of the raspberry to BCM
GPIO.setmode(GPIO.BCM)

# turn off warnings
GPIO.setwarnings(False)

# array of pin numbers
led_pins = [18, 23, 24]

# setup the pins as output
def setup():
        for pin in led_pins:
                GPIO.setup(pin,GPIO.OUT)

def on(pin):
        print "LED on - pin:", pin
        GPIO.output(pin,GPIO.HIGH)

def off(pin):
        print "LED off - pin:", pin
        GPIO.output(pin,GPIO.LOW)

def wait(duration=0.25):
        time.sleep( duration )

def shutdown():
    for pin in led_pins:
            off( pin )


# flicker each light once for a random number
# of iterations
def scheme1():
        # generate a random number of iterations
        # to flash the lights
        iterations= random.randint(3, 15)

        # flash each set of lights attached to the
        # pins (i.e, we turning pins on and off)
        for i in range(iterations):
                for pin in led_pins:
                        on(pin)
                        wait( 0.15 )
                        off(pin)


                        
def flicker(index=0):
        # generate a random number of iterations
        # to flash the lights
        iterations = random.randint(3, 6)

        pin = led_pins[ index ]
        for i in range(iterations):
                on( pin )
                wait(0.1)
                off( pin )
                wait(0.1)
                        
def flicker_all():
        # generate a random number of iterations
        # to flash the lights
        iterations = random.randint(3, 6)

        for i in range(iterations):
                #turn all leds on
                for pin in led_pins:
                        on( pin )

                wait(0.10)

                # turn all leds off
                for pin in led_pins:
                        off( pin )

                wait(0.10)
                

def scheme3():
        # generate a random number of iterations
        # to flash the lights
        iterations= random.randint(3, 15)

        # flash each set of lights attached to the
        # pins (i.e, we turning pins on and off)

        n_pins = len(led_pins)
        for i in range(iterations):
                pin_indices = np.random.choice(n_pins, size=n_pins, replace=False)
                for pin_index in pin_indices:
                        pin = led_pins[ pin_index ]
                        on(pin)
                        wait( 0.15 )
                        off(pin)
             
# execution
setup( )

while True:
        try:
                scheme1( )
                flicker_all()
                flicker( 0 )
                flicker( 1 )
                flicker( 2 )
                flicker_all()
                scheme3( )
        except KeyboardInterrupt:
                shutdown()
                sys.exit(1)
