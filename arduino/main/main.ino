#include <SoftwareSerial.h>
//pins assignment
#define m1_a 3
#define m1_b 5
#define m2_a 6
#define m2_b 9
#define m3_b 11
#define m3_a 10
#define FWD 1
#define BWD 0
#define SRX 8
#define STX 7
#define feedback_m1 A0
#define feedback_m2 A1
#define feedback_m3 A2
#define LED A3
#define RED 4
#define GRN 12
#define BLU 13 

//parameters
#define rec_blink_delay 500
#define max_stroke1 90  //percentage
#define max_stroke2 90  //percentage
#define max_stroke3 90  //percentage
#define min_stroke1 20  //percentage
#define min_stroke2 20  //percentage
#define min_stroke3 20  //percentage

//Macros
#define percent2pwm(x) int(x*2.55)
#define RGB(r,g,b) digitalWrite(RED,r);digitalWrite(GRN,g);digitalWrite(BLU,b);
#define position(x) ((analogRead(x)/1023.0)*100.0)
union{
  float f_val;
  char b_val[4];
  } conv;



SoftwareSerial SSerial(SRX, STX);
int loop_counter=0;
unsigned t=0;
//float setpoint[3]={max_stroke1,max_stroke2,max_stroke3};
float motorPosition[3];
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

char status1,status2,status3;
void loop(){

motorPosition[0]=position(feedback_m1);
motorPosition[1]=position(feedback_m2);
motorPosition[2]=position(feedback_m3);

if (motorPosition[0]>=max_stroke1 && status1=='f'){motor(1,0); }
if (motorPosition[1]>=max_stroke2 && status2=='f'){motor(2,0); }
if (motorPosition[2]>=max_stroke3 && status3=='f'){motor(3,0); }


if (motorPosition[0]<=min_stroke1 && status1=='b'){motor(1,0); }
if (motorPosition[1]<=min_stroke2 && status2=='b'){motor(2,0); }
if (motorPosition[2]<=min_stroke3 && status3=='b'){motor(3,0); }

if(   (millis()-t)>rec_blink_delay ){RGB(LOW,LOW,LOW);}

 
//if(loop_counter++ > 100){
////Serial.print(position(feedback_m1));Serial.print("------");  
////Serial.print(position(feedback_m2)); Serial.print("------");  
////Serial.println(position(feedback_m3));
//Serial.print(motorPosition[2]);Serial.print("---------");Serial.println(status3);
//loop_counter=0; 
//}

int rec=SSerial.read();

switch(rec){

  case 'f':
      motor(1,255); status1='f';      //setpoint[0]=max_stroke1;
      motor(2,255); status2='f';      //setpoint[1]=max_stroke2;
      motor(3,255); status3='f';      //setpoint[2]=max_stroke3;
      blink(GRN);
      break;
      
   case 'b':
      motor(1,-255);  status1='b';    //setpoint[0]=min_stroke1;
      motor(2,-255);  status2='b';    //setpoint[1]=min_stroke2;
      motor(3,-255);  status3='b';    //setpoint[2]=min_stroke3;
      blink(BLU);
      break;
      
   case 's':
      motor(1,0); status1='s';        //setpoint[0]=position(feedback_m1);
      motor(2,0); status2='s';        //setpoint[1]=position(feedback_m2);
      motor(3,0); status3='s';        //setpoint[2]=position(feedback_m3);
      blink(RED);
      break; 

    case 'u':
      motor(3,255); status3='f';      //setpoint[2]=max_stroke3;
      blink(GRN);
      break; 

       case 'j':
      motor(3,-255);  status3='b';    //setpoint[2]=min_stroke3;
      blink(BLU);
      break; 


    case 'i':
      motor(2,255); status2='f';      //setpoint[1]=max_stroke2;
      blink(GRN);
      break; 

       case 'k':
      motor(2,-255);  status2='b';    //setpoint[1]=min_stroke2;
      blink(BLU);
      break; 




    case 'o':
      motor(1,255); status1='f';      //setpoint[0]=max_stroke1;
      blink(GRN);
      break; 

       case 'l':
      motor(1,-255);  status1='b';    //setpoint[0]=min_stroke1;
      blink(BLU);
      break; 



   case 'c':
      motor(1,0); status1='s';        //setpoint[0]=position(feedback_m1);
      blink(RED);
      break; 


    case 'x':
      motor(2,0); status2='s';        //setpoint[1]=position(feedback_m2);
      blink(RED);
      break; 

      case 'z':
      motor(3,0); status3='s';        //setpoint[2]=position(feedback_m3);
      blink(RED);
      break; 
      
  }//switch
 
  }


void blink(int color){

switch(color){
  case RED:
      RGB(HIGH,LOW,LOW);
      t=millis();
  break;
      
  case GRN:
      RGB(LOW,HIGH,LOW);
      t=millis();
  break;

  case BLU:
      RGB(LOW,LOW,HIGH);
      t=millis();
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
    b=m1_b;
    break;
 
  case 2:
    a=m2_a;
    b=m2_b;    
    break;
  
  case 3:
    a=m3_a;
    b=m3_b;
    break;
  
  default:;
}
  
  if(spd>0){   analogWrite(a,spd);  digitalWrite(b,LOW);    } 
  if(spd<0){   analogWrite(b,abs(spd));  digitalWrite(a,LOW);    } 
  if(spd==0){   digitalWrite(b,HIGH);  digitalWrite(a,HIGH);    } 
  }




  
