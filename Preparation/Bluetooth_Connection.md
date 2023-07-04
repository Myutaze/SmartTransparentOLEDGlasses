We first begin with the Bluetooth Connection test.
On the Arduino side we first connected the RX/TX pins
of the Bluetooth Module to the TX/RX of Arduino, the
VCC and GND pins to the Arduino's 5V and GND and turn on the Arduino.
This is only for the test purposes we will change those pins in the code.
Note that the Bluetooth Module HC-05 mainly work seperately from Arduino, the Arduino just receives inputs from it. 

<img align= "left" src = "https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/acc8084e-c597-429b-993e-0c7fcd302b5c" width  = "400" >
 
|     HC-05     |     Arduino   |     
| :-------------: | :-------------: |      
|     RX        |       TX      | 
|     TX        |       RX      |
|     VCC       |       5V      |
|     GND       |       GND     |


<br clear="left"/>
<br>

The Raspberry Pi 3B+ has bluetooth module on-board
but the regular bluetooth connection through settings wouldn't connect directly 
so we first need to install some packages to the Raspberry Pi that will allow us to connect to it.
We install bluez tools with the follwing command on the terminal
of the Raspberry Pi:

```sudo apt-get install bluetooth bluez```

![Rapsberrypi-bluetooth](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/66ba01e8-3aa5-48ec-97b4-740c1d941a5d)



After installing that we need to know our (new) Bluetooth name and its properties.
So in the terminal we type:

```hciconfig```

![hci config](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/132e8ad2-8577-4ce9-9b09-e9e41fe148f5)


You should see "hci0" or an equivalent (hci1, hci2 etc.), Write down that name. We will use it later
Next we scan if we can find any bluetooth devices by typing to the terminal:

```hcitool scan```

![hcitoolscan](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/90449d93-9f28-4abb-ae87-3fd6cbf35916)

You should see a HC-05, which is the bluetooth module that we connected to the Arduino.
We copy the MAC address of it, so mine is 00:19:10:08:29:6F, you copy your own, and then we connect to it with the following command:

```sudo rfcomm connect hci0 00:19:10:08:29:6F```

![connectblue](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/7386bbb8-fc50-4a81-833c-f25236e687d2)



So you should have connected successfully if you have followed the steps correctly. Know that before running any code, be sure to establish the Bluetooth Connection, otherwise the code from the Raspberry Pi side will not work.




