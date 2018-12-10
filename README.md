# handAssist_V3
- The handAssist device has an Arduino Nano, and an ESP8266 WiFi module.
- The WiFi module creats a WiFi access point and acts as a UDP server.
- The device can be connected to a computer using USB. You can write command data on the USB COM port to control the device. 
You can also read feedback data which the device sends every 33 ms (30 Hz).
- The device can also be controlled wirelessly using socket UDP connection.
- The UDP interface is only for controlling the device. The device only listens but does not send data over this interface.

## connection diagram:

![alt text](https://github.com/UAEU-IRI/storage/blob/master/figures/handAssist_diagram.svg "robot_1 frames")


## UDP server details:
- SSID: handAssist
- Password: 12345678
- IP: 192.168.1.10
- Port: 80

## Serial details:
- BaudRate: 115200

## Reading data from HandAssist device
- Device sends data over USB (a USB COM port on the computer).
- Data sent from device are 3 floats which are the poistion of each motor.
- Data are sent as follows:
```
123 55 <pos1[0]> <pos1[1]> <pos1[2]> <pos1[3]> ... <pos3[0]> <pos3[1]> <pos3[2]> <pos3[3]>
```
- Example message:
```
123 55 62 250 72 66 206 59 79 66 246 213 87 66
```

which corresponds to:
```
position 1 = 50.244 mm
position 2 = 51.808 mm
position 3=  53.959 mm
```
- There is a software limit applied on the motor. It can only move between a 20 mm to 90 mm
- total message length is 14 bytes. The first two are framing bytes indicating the start of the message.

where pos1[0]..pos1[3] are the bytes that represents a float value of pos1 (motor 1 position) (IEEE-754 floating point represnetation). pos1[0] is the lowest byte, pos1[3] is the highest byte.

- Example for reading the serial message using Python:
```Python
import serial
import struct

ser = serial.Serial('/dev/ttyUSB0',115200)  # open serial port
data=[]

while True:
    if(ord(ser.read(1))==123):
        if(ord(ser.read(1))==55):
            for i in range(0,12):
                data.append(    ord(ser.read(1) ))
            #convert bytes to floats (12 bytes to 3 floats)
            m1=struct.unpack('f',bytearray(data[0:4]))
            m2=struct.unpack('f',bytearray(data[4:8]))
            m3=struct.unpack('f',bytearray(data[8:12]))
            print m1,',',m2,',',m3
            data=[]


ser.close()             # close port
```



## Command details:
The device can be controlled using either UDP connection, or from the serial port. To control the device, send a character on the serial port, or send the characted on the UDP port (examples are below).
The following table shows what each charater does:

| character     | Action                               |
| ------------- | ------------------------------------ |
| 'f'           |       move all motors forward        |
| 'b'           |       move all motors backward       |
| 's'           |       stop all motors                |
| 'o'           |       move  motor 1 forward          |
| 'i'           |       move  motor 2 forward          |
| 'u'           |       move  motor 3 forward          |
| 'l'           |       move  motor 1 backward         |
| 'k'           |       move  motor 2 backward         |
| 'j'           |       move  motor 3 backward         |
| 'c'           |       stop  motor 1                  |
| 'x'           |       stop  motor 2                  |
| 'z'           |       stop  motor 3                  |

- Python example, sending commands using Serial port: 
```Python
import serial

ser = serial.Serial('/dev/ttyUSB0',115200)  # open serial port
ser.write('s') #stops all motors

ser.close()             # close port
```

- Python UDP client example: 
```Python
import socket

UDP_IP = "192.168.1.10"
UDP_PORT = 80

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto('s', (UDP_IP, UDP_PORT)) #stops all motors


```
