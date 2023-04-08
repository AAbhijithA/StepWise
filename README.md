# StepWise
Your one step application to managing your store using hardware for real time data and assesing its performance via the following functionalities
* Hardware: Arduino UNO and ESP32-Cam for detection of people
* Measurement of footfall in the store aisle
* Measurement of purchase and profits
* Measurement of performance
* Measurement of potential per aisle
- - - -
### Setup
Make the following connections with the Arduino UNO and the ESP32-Cam with the jumper wires as shown below:
![](Connections/Connections.jpg)
After doing the above please go Arduino site and download the Arduino IDE: [Arduino IDE Download](https://www.arduino.cc/en/software)

After the above step then use the code in the ESP32-Loader Directory 
After the above you need to upload the zip file for the "esp32cam.h" library to the Arduino IDE after opening it from the github link given: [Download ZIP](https://github.com/yoursunny/esp32cam)

Then you have to copy paste the following link into the Additional Boards Manager URLs in the *(File>Preferences)*:
```
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json, https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json, http://arduino.esp8266.com/stable/package_esp8266com_index.json
```
After the above go to *(Tools>Board>Boards Manager)* and search for 'esp32' and install it 
and after installation again go to *(Tools>Board>ESP32 Arduino)* and select ESP32 Wrover Module and make sure to set the configurations:
* Upload Speed: 115200
* Flash Frequency: 40MHz
* Flash Mode: QIO
* Partition Scheme: Huge APP (3MB no OTA/1MB SPIFFS)

Run the program and then after **"Hard resetting via RTS pin"** message comes press the reset button on the ESP32-Cam then remove the wires connecting GND and IO0 on the ESP32-Cam and press reset again and you will get a link if the connection to the network happens successfully.