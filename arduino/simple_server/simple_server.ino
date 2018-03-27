#include <ESP8266WiFi.h>

#define ssid "handAssist"
#define password "12345678"

IPAddress local_IP(192,168,1,10);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WiFiServer server(80);

void setup()
{
  Serial.begin(115200);
  Serial.println();
  WiFi.softAPConfig (local_IP, gateway, subnet);
  WiFi.softAP(ssid,password,1,true);

  delay(1000);
  server.begin();
  server.setNoDelay(true);

}

void loop()
{
  WiFiClient client = server.available();
 
  
if (client)
{
while (client.connected()){
  if(client.available()){ Serial.write(client.read());}
if(Serial.available()){ client.write(Serial.read());}
}//while


}//if client



}//void loop
