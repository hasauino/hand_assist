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

## Serial data (sent to computer on hardware serial) details:

Serial.print(motorPosition[0]);Serial.print(",");
Serial.print(motorPosition[1]);Serial.print(",");
Serial.print(motorPosition[2]);Serial.print(",");
Serial.println();

motorPosition[i]: is a float


## UDP commands details:
A UDP client can control the hand by sending characters (1 byte). The following table shows what each charater does:

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

