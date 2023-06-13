We first begin with the Bluetooth Connection.
On the Arduino side we first connected the RX/TX pins
of the Bluetooth Module to the TX/RX of Arduino, the
VCC and GND pins to the Arduino's 5V and GND and turn on the Arduino.
The Raspberry Pi 3B+ has bluetooth module on-board
but the regular bluetooth connection through settings wouldn't connect directly 
so we first need to install some packages to the Raspberry Pi that will allow us to connect to it.
We install bluez tools with the follwing command on the terminal
of the Raspberry Pi:

sudo apt-get install bluetooth bluez

After installing that we need to know our (new) Bluetooth name and its properties.
So in the terminal we type:

hciconfig

You should see "hci0" or an equivalent (hci1, hci2 etc.), Write down that name. We will use it later
Next we scan if we can find any bluetooth devices by typing to the terminal:

hcitool scan

You should



