import RPi.GPIO as GPIO
import phsensor
import sys
import time



PH_UP = 25
PH_DOWN = 8

PH_MIN = 5.5
PH_MAX = 7

def GPIOSetup():
    GPIO.setup(PH_UP, GPIO.OUT, initial = GPIO.HIGH)
    GPIO.setup(PH_DOWN, GPIO.OUT, initial = GPIO.HIGH)
if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        GPIOSetup()
        ph_sensor = phsensor.PHSensor(0,14) #phsensor object
        while True:
            #ph sensing from ad da board
            ph = ph_sensor.read_ph(0)

            #if ph level is below range
            if ph < PH_MIN:
                #turn on PH up pump
                GPIO.output(PH_UP, GPIO.LOW)
                print(f"PH UP pump on at PH:{ph}")
                #time.sleep(pump duration)
                time.sleep(1)
                #turn off PH up pump
                GPIO.output(PH_UP, GPIO.HIGH)
                print("PH UP pump off")

            #if ph level is above range
            if ph > PH_MAX:
                #turn on PH down pump
                GPIO.output(PH_DOWN, GPIO.LOW)
                print(f"PH DOWN pump on at PH:{ph}")
                #time.sleep(pump duration)
                time.sleep(1)
                #turn off PH down pump
                GPIO.output(PH_DOWN, GPIO.HIGH)
                print("PH DOWN pump off")

            #ph sensing interval
            time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit('PH balancing ended')
