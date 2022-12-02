#include "Motor_DC.hpp"

// Constructor
Motor_DC::Motor_DC(uint8_t pinEnable, uint8_t pinA, uint8_t pinB)
{
    this->pinEnable = pinEnable;
    this->pinA = pinA;
    this->pinB = pinB;

    this->InitializatePins();
    this->ChangeSpeed(255);
    this->Stop();
}

// Public
void Motor_DC::RotateRight()
{
    digitalWrite(this->pinA, HIGH);
    digitalWrite(this->pinB, LOW);
}

void Motor_DC::RotateLeft()
{
    digitalWrite(this->pinA, LOW);
    digitalWrite(this->pinB, HIGH);
}

void Motor_DC::Stop()
{
    digitalWrite(this->pinA, LOW);
    digitalWrite(this->pinB, LOW);
}

void Motor_DC::ChangeSpeed(uint8_t speed)
{
    this->speed = speed;
    analogWrite(this->pinEnable, this->speed);
}

// Private
void Motor_DC::InitializatePins()
{
    pinMode(this->pinEnable, OUTPUT);
    pinMode(this->pinA, OUTPUT);
    pinMode(this->pinB, OUTPUT);
}