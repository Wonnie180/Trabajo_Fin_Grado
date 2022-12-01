#include "Motor_DC.hpp"

// Constructor
Motor_DC::Motor_DC(uint8_t pin_enable, uint8_t pin_1, uint8_t pin_2)
{
    this->pin_enable = pin_enable;
    this->pin_1 = pin_1;
    this->pin_2 = pin_2;

    this->InitializatePins();
    this->ChangePWM(255);
    this->Stop();
}

// Public
void Motor_DC::RotateRight()
{
    digitalWrite(this->pin_1, HIGH);
    digitalWrite(this->pin_2, LOW);
}

void Motor_DC::RotateLeft()
{
    digitalWrite(this->pin_1, LOW);
    digitalWrite(this->pin_2, HIGH);
}

void Motor_DC::Stop()
{
    digitalWrite(this->pin_1, LOW);
    digitalWrite(this->pin_2, LOW);
}

void Motor_DC::ChangePWM(uint8_t pwm)
{
    this->pwm = pwm;
    analogWrite(this->pin_enable, this->pwm);
}

// Private
void Motor_DC::InitializatePins()
{
    pinMode(this->pin_enable, OUTPUT);
    pinMode(this->pin_1, OUTPUT);
    pinMode(this->pin_2, OUTPUT);
}