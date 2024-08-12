const int analogIn = A0;
int analogVal=0;

void setup(){
  Serial.begin(9600);
  }

void loop(){
  analogVal=analogRead(analogIn);
  // if(analogVal>400){
  //   Serial.println(1);}
  // else {
  //   Serial.println(0);   }
  Serial.println(analogVal);
  delay(10); 
  }

  
