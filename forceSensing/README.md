# Pins assignment

| force sensor  |  Arduino  |  
|---            |---|
|      VDD      |  5V  |
|      VCC      |   5V |
|      DAT      |   pin 3 |
|      CLK      |   pin 2 |
|      GND      |   GND   |


# Arduino code
- Upload ``` forceSensing.ino ``` sketch on Arduino. The sketch will repeatdely send measured force in Newtons (N).


# Libary
The force sensor is using a load cell amplifier [HX711](https://www.sparkfun.com/products/13879). Library can be downloaded from here (required to combile the ``` forceSensing.ino ``` sketch. Can be downloaded from [here](https://github.com/bogde/HX711).
