#define m1_a 3
#define m1_b 5

#define m2_a 6
#define m2_b 9

#define m3_a 10
#define m3_b 11

#define FWD 1
#define BWD 0

//Macros
#define percent2pwm(x) int(x*2.55)
void setup(){
  Serial.begin(9600);
  pinMode(m1_a,OUTPUT);
  pinMode(m1_b,OUTPUT);
  pinMode(m2_a,OUTPUT);
  pinMode(m2_b,OUTPUT);
  pinMode(m3_a,OUTPUT);
  pinMode(m3_b,OUTPUT);
  }


void loop(){

digitalWrite(m3_a,HIGH);
digitalWrite(m3_b,HIGH); 


digitalWrite(m1_a,LOW);
digitalWrite(m1_b,LOW); 
digitalWrite(m2_a,LOW);
digitalWrite(m2_b,LOW); 
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




  
