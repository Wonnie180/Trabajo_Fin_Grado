char valor = 0b0000;

int latchPin = 9;   // Latch pin of 74HC595 is connected to Digital pin 5
int clockPin = 10;  // Clock pin of 74HC595 is connected to Digital pin 6
int dataPin = 8;    // Data pin of 74HC595 is connected to Digital pin 4

void setup() {
  // put your setup code here, to run once:
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}
int stepdelay = 25;
void loop() {
  // put your main code here, to run repeatedly:
  stepperStep1();
  delay(stepdelay);
  stepperStep2();
  delay(stepdelay);
  stepperStep3();
  delay(stepdelay);
  stepperStep4();
  delay(stepdelay);
  stepperStep5();
  delay(stepdelay);
  stepperStep6();
  delay(stepdelay);
  stepperStep7();
  delay(stepdelay);
  stepperStep8();
  delay(stepdelay);
}


void updateShiftRegister() {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, valor);
  digitalWrite(latchPin, HIGH);
}

void stepperStep1() {
  // A+
  valor = 0b1000;
  updateShiftRegister();
}

void stepperStep2() {
  // A+,B+
  valor = 0b1100;
  updateShiftRegister();
}

void stepperStep3() {
  // B+
  valor = 0b0100;
  updateShiftRegister();
}

void stepperStep4() {
  // A-,B+
  valor = 0b0110;
  updateShiftRegister();
}

void stepperStep5() {
  // A-
  valor = 0b0010;
  updateShiftRegister();
}

void stepperStep6() {
  // A-,B-
  valor = 0b0011;
  updateShiftRegister();
}

void stepperStep7() {
  // B-
  valor = 0b0001;
  updateShiftRegister();
}

void stepperStep8() {
  // A+, B-
  valor = 0b1001;
  updateShiftRegister();
}

// void stepperStep1() {
//   // A+,B+
//   valor = 0b1100;
//   updateShiftRegister();
// }

// void stepperStep2() {
//   // A+,B-
//   valor = 0b1001;
//   updateShiftRegister();
// }

// void stepperStep3() {
//   // A-,B-
//   valor = 0b0011;
//   updateShiftRegister();
// }

// void stepperStep4() {
//   // A-,B+
//   valor = 0b0011;
//   updateShiftRegister();
// }