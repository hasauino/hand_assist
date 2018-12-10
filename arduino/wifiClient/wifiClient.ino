#include <ESP8266WiFi.h>

#define SSID "handAssist"
#define PASSWORD "12345678"
#define POSRT 80
IPAddress SERVER_IP(192,168,1,10);

WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(10);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500); }//while

}//setup



void loop() {
//reconnect if disconnected
if(!client.connected()){
 client.connect(SERVER_IP, POSRT);
 delay(100); 
  }


if(Serial.available()){
  client.write(Serial.read());  
  }//if


}//loop
