#include <Arduino.h>

#include "../lib/Led/Led/Led.hpp"
#include "../lib/Motor/Motor_DC/Motor_DC.hpp"
#include "../lib/Tropa/Tropa/Tropa.hpp"


Led led = Led(2);
Motor_DC motor_izq = Motor_DC(15,4,5); // D15, D4, RX2 | EnableA, In1, In2
// Motor_DC motor_Der = Motor_DC(22,27,34); // D2, TX2, D5 | EnableB, In3, In4

Tropa tropa = Tropa(1, led, motor_izq, motor_izq);


void setup()
{
  Serial.begin(9600);
}

void loop()
{  
  tropa.Change_Color(255,255,255);
  delay(2000);
  tropa.Change_Color(0,0,0);
  delay(2000);
}
