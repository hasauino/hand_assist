/*
This code is to be executed on the ESP12 connected to the RPi
 */
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

#define SSID "handAssist"
#define PASSWORD "12345678"
#define PORT 80
IPAddress SERVER_IP(192,168,1,10);

WiFiUDP udb;

void setup() {
  Serial.begin(115200);
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500); }//while

}//setup



void loop() {

if(Serial.available()){
if(udb.beginPacket(SERVER_IP, PORT)){
   udb.write(Serial.read());
   udb.endPacket();
  }//if udb_begin

}//if serial available


}//loop
