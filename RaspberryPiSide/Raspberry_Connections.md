So on the Raspberry Pi side we implement the security alert part.
The idea is that when there is an intruder in the house or in your company you will get alerted
and the alert message will be displayed on the transparent screen. When someone is detected from the motion sensor
it will prompt the detected person to enter a code, if he times out or enters the wrong password, 
it will be considered an intruder and send a message to the smart glasses.
Here is the GPIO ports:

<img src = "https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/4bff3b20-5b0f-42ac-a685-668e1360b900" width="400" >



# The PIR Motion Sensor

|     Motion Sensor     |     Raspberry Pi   |
| :-------------: | :-------------: |
|     VCC      |       Any 5V Pin      |
|     GND       |      Any Ground Pin      |
|     OUT       |       GPIO23     |

# The Numpad

The Numpad has 8 pins for 4 rows and 4 columns. We do a combination of rows and columns to get the number we want,
similar to a 4x4 matrix, we can say that the position (2,3) contains the number 6. Now for our Numpad we defined:
Out of 8 pins on the numpad, the first 4 pins are the rows, the last 4 pins are the columns like this:

<img src = "https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/dfbcd2f3-e66e-46a6-b21a-573d943994d6" width = 400>


- The Rows: GPIO5, GPIO6, GPIO13, GPIO19

- The Colmuns: GPIO12, GPIO16, GPIO20, GPIO21


Here how it looks:


![Raspberry Pi  + Numpad + Sensor ](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/0fbda0ae-ae1f-40d8-9b51-ac4729677f79)


# API

Weather and Currency Exchange info from the internet through API. 
The 2 websites i used for this are:

- Openweathermap.com

- freecurrencyapi.net (which became currencyapi.com)

You don't have to choose those 2 websites you can choose any provider. You will need to read the documentation of those provider on how to get the API links or keys.


