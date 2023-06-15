#We install and import these packages
import serial
import time
from time import sleep
import requests
import json
import RPi.GPIO as GPIO

# these GPIO pins are connected to the keypad
# change these according to your connections in case you decided to put on different GPIOs!
L1 = 5
L2 = 6
L3 = 13
L4 = 19

L = [L1,L2,L3,L4] #This is our Rows of the Keypad

C1 = 12
C2 = 16
C3 = 20
C4 = 21

C = [C1,C2,C3,C4] #This is our Columns of the Keypad

R = 23 #This is for our Motion Sensor


# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(L[i], GPIO.OUT)
    GPIO.setup(C[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R, GPIO.IN) 

#Before running this code, make sure you are connected with Bluetooth from the terminal, when we ran this command:
#sudo rfcomm connect hci0 00:19:10:08:29:6F (explanation on the Preparation)

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate= 9600 ) #This is for sending data via Bluetooth, we use as if we were passsing the data through a serial port

# This jprint function is just used to see the API(JSON) data in a more readable way
def jprint(obj):
	text = json.dumps(obj, sort_keys=True , indent=4)
	print(text)
#We start an infinite loop to continously make the code work
while True:
    response = requests.get("place your weather API link here for the weather of the city you want")
    weather = response.json()
    
    response = requests.get("Place your currency API link here, my link here is to give the Exchange Currency of Dollar")
    currencyUSD = response.json()
    response = requests.get("Place your currency API link here, my link here is to give the Exchange Currency of Euro")
    currencyEUR = response.json()
    response = requests.get("Place your currency API link here, my link here is to give the Exchange Currency of Pound")
    currencyGBP = response.json()
    
#For the Weather info, we receive plenty of data but we are only interested in the following data:
#the city's name we want the weather of,
#The temperature
#The weather condition (Raining, cloudy etc.)
#The detailed weather Condition (Harsh Raining, Thick fog etc.)

	
    city = str(weather['list'][0]['name']) # from the json data we retrive the name of the city

    celcius = str(weather['list'][0]['main']['temp']) # from the json data we retrive the temperature in Celcius

    basic = str(weather['list'][0]['weather'][0]['main']) # from the json data we retrive the weather condition

    detail = str(weather['list'][0]['weather'][0]['description']) # from the json data we retrive the detailed weather condition

#For the currency exchange, when we retrieve data for one currency, it will usually give the list of currency exchange for that one particular currency,
# you can choose which currency you want to compare. In my case i will compare Dollar, Euro and Pound to TL. So it will give me the data of
# 1 USD/EUR/GPT = XX TL 

    USD = str(currencyUSD['data']['TRY']) # Dollar - TL data
    EUR = str(currencyEUR['data']['TRY']) # Euro - TL data
    GBP = str(currencyGBP['data']['TRY']) # Great Britain Pound - TL data

#This is to print in our Raspberry Pi python IDE terminal to see the data
    print(city)
    print(celcius)
    print(basic)
    print(detail)

    print("1 USD = ",USD, "TRY")
    print("1 EUR = ",EUR, "TRY")
    print("1 GBP = ",GBP, "TRY")


#We count the data's length for each and then send these length to Arduino to make it know that for a particular data, it will receive X amount of characters
    c = str(len(str(city))) #count the number of character in the city's name so for example Ankara would be 6
    t = str(len(str(celcius)))
    b = str(len(str(basic)))
    d = str(len(str(detail)))

    count = 1 #This variable is used so we can break the loop when 4 number are entered
    P = [] #This variable will register the entered keys from the Keypad
    i = 0 #This variable is used to count how many numbers we entered so far (so each time a number is entered this will increase by one)
    S = [] # This variable is used to join all the numbers entered and check whether the password is correct or not 
    C = 0
    D = 0 # This variable is used to check if the motion sensor detected something, and in case it did, the motion sensor will send 1 as a signal
    A = 0 # This variable is used to check whether the password was entered correctly, if it did not it will become '1' to signal that a wrong password was entered
	  # or timeout occured

# We start a timer here, the sensor works for 30 seconds and if no movement is detected, it will proceed to send data we collected over bluetooth to the Arduino,
# However if a motion was detected, the keypad will begin working and the individual has 10 seconds to enter the code, if it enters the correct password (1234 in my case)
# then an alert is not given, however if the password is wrong or timeout the intruder alert will be sent to notify the smart glass user. 

    start_time = time.time()
    seconds = 30
    second = 10

    while count == 1:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if(GPIO.input(R) == 1): #activate the keypad in case a motion was detected from the PIR sensor
            print ("Intruder detected")
            D = 1
            time.sleep(1)
            count = 2
        if elapsed_time > seconds: #break loop if 30 seconds have passed
            count = 2
            
    time.sleep(1)
    start_time = time.time()
   
    if(D == 1):
        print("Enter code:", end=" ")
        while(D == 1):
    
                current_time = time.time()
                elapsed_time = current_time - start_time #We check the elapsed time 

                if elapsed_time > second: #If the elapsed time goes beyond 10 seconds the break the loop and register an intruder alert.
                    A = 1
                    print("Intruder Alert!!!")
                    D = 2
                    count == 2
         #Here is where we code the input we receive from the keypad, you can look online at the logic how the keypad works  
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

               
#We check the password here whether is correct or not
                if i == 4:
                    print("")
                    S = ''.join(map(str,P))
                    if (S != "1234"):  #we define our password as '1234' and if its not the case we register an intruder alert
                        A = 1
                        print("Intruder Alert!!!")
                    D = 2
                    count = 2
                    print(S)
      
    
    # We send all the data over bluetooth to Arduino
    bluetoothSerial.write(bytes("a", 'utf-8')) #We send something to Arduino to know that there is incomming data so be prepared to receive it
    time.sleep(0.5) # we put some delays here and there because the Arduino can't process fast enough and cause problems when its receiving data
    bluetoothSerial.write(bytes(c, 'utf-8')) #We send how many characters the Arduino will receive about the city so to make him know to expect that much character
					      #for that particular data so 6 for Ankara 
    bluetoothSerial.write(bytes(city, 'utf-8')) # We send the data 'Ankara' to Arduino, in the Arduino's side it will see that it received 6 character data 
						#so it will stop waiting to receive more data for the city information and proceed to the next line to receive data
						# about the temperature
    bluetoothSerial.write(bytes(celcius, 'utf-8')) #For numerals its a direct send.
    time.sleep(1.2)
#We do the same for the rest
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
        bluetoothSerial.write(bytes("1", 'utf-8')) # in case there is an intruder '1' will be send to Arduino to make it know there is an intruder alert.
    

    
    
    
    







    
