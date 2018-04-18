#include <SoftwareSerial.h>
//pins assignment
#define m1_b 3
#define m1_a 5
#define m2_b 6
#define m2_a 9
#define m3_a 11
#define m3_b 10
#define FWD 1
#define BWD 0
#define SRX 8
#define STX 7
#define feedback_m1 A0
#define LED A3
#define RED 4
#define GRN 12
#define BLU 13 

//parameters
#define rec_blink_delay 250

//Macros
#define percent2pwm(x) int(x*2.55)
#define RGB(r,g,b) digitalWrite(RED,r);digitalWrite(GRN,g);digitalWrite(BLU,b);
union{
  float f_val;
  char b_val[4];
  } conv;


SoftwareSerial SSerial(SRX, STX);
int loop_counter=0;
void setup(){
  Serial.begin(115200);
  SSerial.begin(115200);
  pinMode(m1_a,OUTPUT);
  pinMode(m1_b,OUTPUT);
  pinMode(m2_a,OUTPUT);
  pinMode(m2_b,OUTPUT);
  pinMode(m3_a,OUTPUT);
  pinMode(m3_b,OUTPUT);
  pinMode(LED,OUTPUT);
  pinMode(RED,OUTPUT);
  pinMode(GRN,OUTPUT);
  pinMode(BLU,OUTPUT);  
  pinMode(feedback_m1,INPUT);

  digitalWrite(LED,HIGH);
  }


void loop(){
if(loop_counter++ > 1000){
conv.f_val=(analogRead(feedback_m1)/1023.0)*100.0;
Serial.println(conv.f_val); loop_counter=0;

//SSerial.write(123);
//SSerial.write(55);
//SSerial.write(conv.b_val[0]);
//SSerial.write(conv.b_val[1]);
//SSerial.write(conv.b_val[2]);
//SSerial.write(conv.b_val[3]);

}

int rec=SSerial.read();

switch(rec){

  case 'f':
      motor(1,255);
      motor(2,255);
      motor(3,255);
      blink(GRN);
      break;
      
   case 'b':
      motor(1,-255);
      motor(2,-255);
      motor(3,-255);
      blink(BLU);
      break;
      
   case 's':
      motor(1,0);
      motor(2,0);
      motor(3,0);
      blink(RED);
      break; 

    case 'u':
      motor(3,255);
      blink(RED);
      break; 

       case 'j':
      motor(3,-255);
      blink(RED);
      break; 


    case 'i':
      motor(2,255);
      blink(RED);
      break; 

       case 'k':
      motor(2,-255);
      blink(RED);
      break; 




    case 'o':
      motor(1,255);
      blink(RED);
      break; 

       case 'l':
      motor(1,-255);
      blink(RED);
      break; 


      
  }//switch
  
  }


void blink(int color){

switch(color){
  case RED:
      RGB(HIGH,LOW,LOW);
      delay(rec_blink_delay);  
      RGB(LOW,LOW,LOW);
  break;
      
  case GRN:
      RGB(LOW,HIGH,LOW);
      delay(rec_blink_delay);  
      RGB(LOW,LOW,LOW);
  break;

  case BLU:
      RGB(LOW,LOW,HIGH);
      delay(rec_blink_delay);  
      RGB(LOW,LOW,LOW);
  break;
  }


 }



void motor(int ID,float spd){
int a,b;
if(spd>255){spd=255;}
if(spd<-255){spd=-255;}
switch (ID) {
  case 1:
    a=m1_a;
    b=m2_a;
    break;
 
  case 2:
    a=m1_b;
    b=m2_b;    
    break;
  
  case 3:
    a=m3_a;
    b=m3_b;
    break;
  
  default:
    Serial.println("please enter a valid motor ID");
}
  
  if(spd>0){   analogWrite(a,spd);  digitalWrite(b,LOW);    } 
  if(spd<0){   analogWrite(b,abs(spd));  digitalWrite(a,LOW);    } 
  if(spd==0){   digitalWrite(b,HIGH);  digitalWrite(a,HIGH);    } 
  }




  
