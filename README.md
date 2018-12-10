# handAssist_V3

## connection diagram:

Computer <-- Hardware serial --> Arduino Nano (main controller) <--  Soft Serial --> ESP8266 WiFi Module (UDP server)<--(UDP connection)--> mobile app (or any UDP client)

## UDP server details:
- SSID: handAssist
- Password: 12345678
- IP: 192.168.1.10
- Port: 80

## Hardware and Soft serial details:
- BaudRate: 115200

## Serial data (sent to computer on hardware serial) framing details:
- Data are sent as follows:
<123> <55> <position1[0]> <position1[1]> <position1[2]> <position1[3]> ... <position3[0]> <position3[1]> <position3[2]> <position3[3]>

where position1[0]..position1[3] are the bytes that represents a float value of position1 (motor 1 position) (IEEE-754 floating point represnetation). position1[0] is the loaest byte, position1[3] is the highest byte.

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
# send a 's' charachter to the hand. Will cause all motors to stop.
import socket

UDP_IP = "192.168.1.10"
UDP_PORT = 80

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto('s', (UDP_IP, UDP_PORT))


```

- Python UDP client example: 
```Python
# send a 's' charachter to the hand. Will cause all motors to stop.
import socket

UDP_IP = "192.168.1.10"
UDP_PORT = 80

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto('s', (UDP_IP, UDP_PORT))


```
