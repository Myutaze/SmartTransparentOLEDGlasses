The full connection of the Arduino Side looks like this:

<img src = "https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/6a333a73-cccb-469b-bf68-e41abca8c3f6" width = "350">

Connect to the Arduino the modules with the help of a breadboard.

In Arduino code the connection ports will explained but here is a few of them on to which ports to connect them:

## Toled Screen Connection

There are 7 pins on the TOLED board: GND, VCC, SCL, SDA(or SDAIN), RST, SA0(or D/C), CS. We only use 5 of those.

  
|     Toled     |     Arduino   |
| :-------------: | :-------------: |
|     SCL       |       Pin A5      |
|     SDA       |       Pin A4      |
|     GND       |       GND     |
|     VCC       |       5V      |
|     RST       |      RESET    |

  

## RTC Module Connection

|      RTC      |     Arduino   |
| :-------------: | :-------------: |
|     VCC       |  3.3V or 5V   |
|     GND       |      GND      |
|     CLK       |      Pin 4    |
|     DATA      |      Pin 5    |
|     RST       |      Pin 6    |


# Bluetooth Module

|      HC-05      |     Arduino   |
| :-------------: | :-------------: |
|     VCC       |       5V      |
|     GND       |      GND      |
|     RX        |      Pin 11(TX)   |
|     TX        |     Pin 10(RX)    |

On Arduino we will define the RX/TX as pin 10/11

# Infra-red Sensor


|      HW-201      |     Arduino   |
| :-------------: | :-------------: |
|     VCC       |       3.3V or 5V      |
|     GND       |      GND      |
|     OUT        |      Pin 7   |




