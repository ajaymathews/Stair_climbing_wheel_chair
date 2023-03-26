#define joyX A0
#define joyY A5

int button=2;
int buttonState = 0;
int buttonState1 = 0;

void setup() {
  pinMode(7,OUTPUT);
  pinMode(button,INPUT);
  digitalWrite(button, HIGH);
  Serial.begin(9600);
}
 
void loop() {
 int xValue = analogRead(joyX);
 int yValue = analogRead(joyY);
 
//  Serial.print(xValue);
//  Serial.print(":");
//  Serial.println(yValue);
  
  buttonState = digitalRead(button);
  //Serial.println(buttonState);
  if (xValue>=0 && yValue<=10)
  {
     Serial.print("D");
  }
  if (xValue<=10 && yValue>=500)
  {
    Serial.print("W");
  }


  if (xValue>=1020 && yValue>=500)
  {
    Serial.print("S");
  }


  if (xValue>=500 && yValue>=1020)
  {
    Serial.print("A");
  }
 if (xValue>=480 && xValue<=540 && yValue>=480 && yValue<=540 )
{
  Serial.print("X");
}

  if (buttonState == LOW)
  {
    Serial.println("Switch = High");
  }
  buttonState1 = digitalRead(7);
  delay(50);
}
