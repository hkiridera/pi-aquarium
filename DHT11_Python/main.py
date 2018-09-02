import ambient
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

ambi = ambient.Ambient("<channelID>", "<apikey>") 

while True:
    result = instance.read()
    if result.is_valid():
        json={}
#        print("Last valid input: " + str(datetime.datetime.now()))
#        print("Temperature: %d C" % result.temperature)
#        print("Humidity: %d %%" % result.humidity)
        json["d1"]=result.temperature
        json["d2"]=result.humidity
        print(json)
        try:
          ambi.send(json)
        except Exception:
          pass
    time.sleep(300)
