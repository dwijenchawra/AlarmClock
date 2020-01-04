from gpiozero import Button
from gpiozero import Motor

import time

print(time.strftime("%H"))
print(time.strftime("%M"))
print(time.strftime("%S"))


button = Button(2)
motor = Motor(forward=23, backward=24)

minute = "30"
hour = "07"

timeToStop = 60

currentTime = None
alarmCleared = False

def main():
    while True:
        global currentTime
        global alarmCleared

        print(str(time.strftime("%H")) + " " + str(time.strftime("%M")) + " " + str(time.strftime("%S")))
        print(hour + " " + minute)

        if time.strftime("%M") > minute:
            alarmCleared = False

        time.sleep(0.5)

        if time.strftime("%M") == minute and time.strftime("%H") == hour and alarmCleared == False:
            motor.forward()
            print("in main loop for alarm")

            while True:
                motor.forward()

                currentTime = time.time()
                print(currentTime)
                time.sleep(0.5)

                while button.is_pressed:
                    motor.stop()
                    print(str(currentTime) + "  button pressed")
                    time.sleep(0.5)

                    if int(time.time()) > int(currentTime) + timeToStop:
                        alarmCleared = True
                        print("done?")
                        motor.forward()
                        time.sleep(2)
                        motor.stop()
                        break
                    
                if int(time.time()) > int(currentTime) + timeToStop:
                    break
                

                



    


if __name__ == "__main__":
    main()

