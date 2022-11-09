import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import speech_recognition as sr
GPIO.setmode(GPIO.BCM)


def temperatureAndHumidity():
    GPIO.setmode(GPIO.BCM)
    h_sensor = Adafruit_DHT.DHT11
    DHT_PIN = 15
    humidity, temperature = Adafruit_DHT.read(h_sensor, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity{1:0.1f}%".format(temperature, humidity))
        return temperature, humidity

    else:
        print('Sensor fail. Check wiring.')


def waterSensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    return GPIO.input(4) == 1


def LightSensor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)
    return GPIO.input(14) == 1


def servo(direc, times):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 50)
    print('Start')
    # 2-6, 7stop, 8-13
    pwm.start(direc)

    time.sleep(times)
    print('Stop')
    pwm.stop()
    GPIO.cleanup()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talking...")
        audio_text = r.record(source, duration=5)
        print("Time over, thanks!")
        try:
            result=r.recognize_google(audio_text, language="en-us")
            return result

        except:
            return "sorry, I did not get that"


'''def main():
    condition=True
    while condition:
        user = str(input("your mode:"))

        if "stop" in user:
            condition=False

        elif "natural" in user:
            servo(2, 5)

        elif "auto" in user:
            innerCondition=True
            while innerCondition:
                temperature, humidity = temperatureAndHumidity()
                isLight = LightSensor()
                isRain = waterSensor()
                print("Temp=%d, Humid=%d"%(temperature,humidity)+str(isLight)+str(isRain))
                if temperature >= 21 and humidity <= 0.7 and isLight and not isRain:
                    servo(2,5)

                else:
                    servo(13,5)
                user2= str(input("your mode:"))
                if "quit" in user2:
                    break
                else:
                    pass
            

        elif "dry" in user:
            servo (13,5)

    print("Thanks For Using!")'''

def main():
    r = sr.Recognizer()
    condition = True
    while condition:
        with sr.Microphone() as source:
            print("Talking...")
            audio_text = r.record(source, duration=5)
            print("Time over, thanks!")
            user = r.recognize_google(audio_text)
            try:
                if "stop" in user:
                    condition = False

                elif "natural" in user:
                    servo(2, 5)

                elif "auto" in user:
                    innerCondition = True
                    while innerCondition:
                        temperature, humidity = temperatureAndHumidity()
                        isLight = LightSensor()
                        isRain = waterSensor()
                        print("Temp=%d, Humid=%d" % (temperature, humidity) + str(isLight) + str(isRain))
                        if temperature >= 21 and humidity <= 0.7 and isLight and not isRain:
                            servo(2, 5)

                        else:
                            servo(13, 5)
                        user2 = listen()
                        if "quit" in user2:
                            break
                        else:
                            pass


                elif "dry" in user:
                    servo(13, 5)
            except:
                print("sorry, I did not get that")
    print("Thanks for using!")




main()