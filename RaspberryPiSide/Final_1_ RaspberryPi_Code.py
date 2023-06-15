import serial
import time
from time import sleep
import requests
import json
import RPi.GPIO as GPIO

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 5
L2 = 6
L3 = 13
L4 = 19

L = [L1,L2,L3,L4]

C1 = 12
C2 = 16
C3 = 20
C4 = 21

C = [C1,C2,C3,C4]

R = 23


# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(L[i], GPIO.OUT)
    GPIO.setup(C[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R, GPIO.IN) 
#sudo rfcomm connect hci0 00:19:10:08:29:6F
bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate= 9600 )

def jprint(obj):
	text = json.dumps(obj, sort_keys=True , indent=4)
	print(text)

while True:
    response = requests.get("https://api.openweathermap.org/data/2.5/find?q=Ankara&units=metric&appid=7e0d145d3a696ff777f00fb0d5280b7f")
    weather = response.json()
    
    response = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=8bd030f0-6676-11ec-a458-01d0b9d4c1ef&base_currency=USD")
    currencyUSD = response.json()
    response = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=8bd030f0-6676-11ec-a458-01d0b9d4c1ef&base_currency=EUR")
    currencyEUR = response.json()
    response = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=8bd030f0-6676-11ec-a458-01d0b9d4c1ef&base_currency=GBP")
    currencyGBP = response.json()
    
    


    city = str(weather['list'][0]['name'])

    celcius = str(weather['list'][0]['main']['temp'])

    basic = str(weather['list'][0]['weather'][0]['main'])

    detail = str(weather['list'][0]['weather'][0]['description'])

    USD = str(currencyUSD['data']['TRY'])
    EUR = str(currencyEUR['data']['TRY'])
    GBP = str(currencyGBP['data']['TRY'])

    print(city)
    print(celcius)
    print(basic)
    print(detail)

    print("1 USD = ",USD, "TRY")
    print("1 EUR = ",EUR, "TRY")
    print("1 GBP = ",GBP, "TRY")



    c = str(len(str(city))) #count the number of character in the city's name
    t = str(len(str(celcius)))
    b = str(len(str(basic)))
    d = str(len(str(detail)))

    count = 1
    P = []
    i = 0
    S = []
    C = 0
    D = 0
    A = 0


    start_time = time.time()
    seconds = 30
    second = 10

    while count == 1:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if(GPIO.input(R) == 1):
            print ("Intruder detected")
            D = 1
            time.sleep(1)
            count = 2
        if elapsed_time > seconds:
            count = 2
            
    time.sleep(1)
    start_time = time.time()
    
    if(D == 1):
        print("Enter code:", end=" ")
        while(D == 1):
    
                current_time = time.time()
                elapsed_time = current_time - start_time

                if elapsed_time > second:
                    A = 1
                    print("Intruder Alert!!!")
                    D = 2
                    count == 2
        
                GPIO.output(L1, GPIO.HIGH)

                if GPIO.input(C1) == 1:
                    print('1', end="")
                    P.append(1)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C1) == 1:
                    pass
    
                if GPIO.input(C2) == 1:
                    print('2', end="")
                    P.append(2)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C2) == 1:
                    pass

                if GPIO.input(C3) == 1:
                    print('3', end="")
                    P.append(3)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C3) == 1:
                    pass
   
                GPIO.output(L1, GPIO.LOW)

                GPIO.output(L2, GPIO.HIGH)

                if GPIO.input(C1) == 1:
                    print('4', end="")
                    P.append(4)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C1) == 1:
                    pass
    
                if GPIO.input(C2) == 1:
                    print('5', end="")
                    P.append(5)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C2) == 1:
                    pass

                if GPIO.input(C3) == 1:
                    print('6', end="")
                    P.append(6)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C3) == 1:
                    pass

   
                GPIO.output(L2, GPIO.LOW)

    
                GPIO.output(L3, GPIO.HIGH)

                if GPIO.input(C1) == 1:
                    print('7', end="")
                    P.append(7)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C1) == 1:
                    pass
    
                if GPIO.input(C2) == 1:
                    print('8', end="")
                    P.append(8)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C2) == 1:
                    pass

                if GPIO.input(C3) == 1:
                    print('9', end="")
                    P.append(9)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C3) == 1:
                    pass
   
                GPIO.output(L3, GPIO.LOW)

    
                GPIO.output(L4, GPIO.HIGH)
        
                if GPIO.input(C2) == 1:
                    print('0', end="")
                    P.append(0)
                    i = i + 1
                    time.sleep(0.2)
                while GPIO.input(C2) == 1:
                    pass
   
   
                GPIO.output(L4, GPIO.LOW)

                #GPIO.output(L, GPIO.HIGH)
    
                #if(GPIO.input(C4) == 1):
                    #print('Finished', end=" ")
                    #S = ''.join(map(str,P))
                    #print(S)
                    #D = 2
                    #A = 1
                    #count = 2
        
                #GPIO.output(L, GPIO.LOW)
    

                if i == 4:
                    print("")
                    S = ''.join(map(str,P))
                    if (S != "1234"):
                        A = 1
                        print("Intruder Alert!!!")
                    D = 2
                    count = 2
                    print(S)
      
    
    
    bluetoothSerial.write(bytes("a", 'utf-8'))
    time.sleep(0.5)
    bluetoothSerial.write(bytes(c, 'utf-8'))
    bluetoothSerial.write(bytes(city, 'utf-8'))
    bluetoothSerial.write(bytes(celcius, 'utf-8'))
    time.sleep(1.2)
    bluetoothSerial.write(bytes(b, 'utf-8'))
    bluetoothSerial.write(bytes(basic, 'utf-8'))
    time.sleep(1)
    bluetoothSerial.write(bytes(d, 'utf-8'))
    bluetoothSerial.write(bytes(detail, 'utf-8'))
    bluetoothSerial.write(bytes(USD, 'utf-8'))
    time.sleep(1.1)
    bluetoothSerial.write(bytes(EUR, 'utf-8'))
    time.sleep(1.1)
    bluetoothSerial.write(bytes(GBP, 'utf-8'))
    time.sleep(1.5)
    if A == 1:
        bluetoothSerial.write(bytes("1", 'utf-8'))
    

    
    
    
    







    
