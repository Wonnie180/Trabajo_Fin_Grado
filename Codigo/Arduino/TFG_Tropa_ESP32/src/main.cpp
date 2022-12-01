#include <Arduino.h>
#include <Led.hpp>
#include <Motor_DC.hpp>

// Led led = Led(2);

Motor_DC motor_izq = Motor_DC(15,2,5); // D15, D4, RX2 | EnableA, In1, In2
// Motor_DC motor_Der = Motor_DC(22,27,34); // D2, TX2, D5 | EnableB, In3, In4

// Motor A connections
int enA = 15;
int in1 = 2;
int in2 = 4;


void setup()
{
  Serial.begin(9600);
}

void loop()
{  
  motor_izq.RotateLeft();
  delay(2000);
  motor_izq.RotateRight();
  delay(2000);
}
