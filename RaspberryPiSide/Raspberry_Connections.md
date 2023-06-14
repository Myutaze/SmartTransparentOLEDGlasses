So on the Raspberry Pi side we implement the security alert part.
The idea is that when there is an intruder in the house or in your company you will get alerted
and the alert message will be displayed on the transparent screen. When someone is detected from the motion sensor
it will prompt the detected person to enter a code, if he times out or enters the wrong password, 
it will be considered an intruder and send a message to the smart glasses.

So here is the connection for them:

# The PIR Motion Sensor

|     Motion Sensor     |     Raspberry Pi   |
| :-------------: | :-------------: |
|     VCC      |       Any 5V Pin      |
|     GND       |      Any Ground Pin      |
|     OUT       |       GPIO23     |

You can check online the pinout of the Raspberry Pi 3B+

# The Numpad





Weather and Currency Exchange info from the internet through API. 
The 2 websites i used for this are 

- Openweathermap.com
- freecurrencyapi.net (which became currencyapi.com)

You don't have to choose those 2 websites you can choose any provider. You will need to read the documentation of those provider on how to get the API links or keys.

As for th
