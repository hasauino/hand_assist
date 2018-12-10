/*
This code is to be executed on ESP12 wifi module 
connected to the Arduino of the hand assistive device
*/

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#define ssid "handAssist"
#define password "12345678"

IPAddress local_IP(192,168,1,10);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WiFiServer server(80);
WiFiUDP udb;

void setup()
{
  Serial.begin(115200);
  Serial.println();
  WiFi.softAPConfig (local_IP, gateway, subnet);
  WiFi.softAP(ssid,password,1,false);//SSID,Pass,channelNo.,hidden or shown 

  delay(1000);
  server.begin();
  server.setNoDelay(true);

  udb.begin(80);


}

void loop()
{
 
if (udb.parsePacket()>0){
  Serial.write(udb.read());}
}//void loop
