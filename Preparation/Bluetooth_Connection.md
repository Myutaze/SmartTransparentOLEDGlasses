We first begin with the Bluetooth Connection.
On the Arduino side we first connected the RX/TX pins
of the Bluetooth Module to the TX/RX of Arduino, the
VCC and GND pins to the Arduino's 5V and GND and turn on the Arduino.

<img src = "https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/4bea568e-54ef-4d7e-86c7-71c4c25ffaff" width  = "400" >

The Raspberry Pi 3B+ has bluetooth module on-board
but the regular bluetooth connection through settings wouldn't connect directly 
so we first need to install some packages to the Raspberry Pi that will allow us to connect to it.
We install bluez tools with the follwing command on the terminal
of the Raspberry Pi:

```sudo apt-get install bluetooth bluez```

![Rapsberrypi-bluetooth](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/10dfd4c8-daa2-4ef0-809e-6990164972d7)


After installing that we need to know our (new) Bluetooth name and its properties.
So in the terminal we type:

```hciconfig```

![hci config](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/3d573547-e8ea-4bfa-9b9b-b41acac4cc63)

You should see "hci0" or an equivalent (hci1, hci2 etc.), Write down that name. We will use it later
Next we scan if we can find any bluetooth devices by typing to the terminal:

```hcitool scan```

![hcitoolscan](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/1cf72ba5-fffc-4029-a3be-a6c66c166339)

You should see a HC-05, which is the bluetooth module that we connected to the Arduino.
We copy the MAC address of it, so mine is 00:19:10:08:29:6F, you copy your own, and then we connect to it with the following command:

```sudo rfcomm connect hci0 00:19:10:08:29:6F```

![connectblue](https://github.com/Myutaze/SmartTransparentOLEDGlasses/assets/123553691/25fbd89b-7949-46ec-af2b-6aa8261cc32f)


So you should have connected successfully if you have followed the steps correctly.
