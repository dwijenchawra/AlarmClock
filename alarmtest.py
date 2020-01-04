import time

print(time.strftime("%I"))
print(time.strftime("%M"))
print(time.strftime("%S"))


motorIn = 5
motorOut = 6
button = 10

currentMins = None
currentSecs = None

def main():
    while True:
        global currentMins
        global currentSecs

        print(time.strftime("%I") + time.strftime("%M") + time.strftime("%S"))


        if time.strftime("%M") == "59" and time.strftime("%I") == "07":
            print("motor on")

            while time.strftime("%M") == 15:
                currentMins = time.strftime("%M")
                currentSecs = time.strftime("%S")

                while True:
                    print("motor off")
                    
                    if time.strftime("%M") > currentMins and time.strftime("%S") > currentSecs:
                        print("motor on for 2 secs")
                        time.sleep(2)
                        break
                    
                if time.strftime("%M") > currentMins and time.strftime("%S") > currentSecs:
                    break
                

                



    


if __name__ == "__main__":
    main()
