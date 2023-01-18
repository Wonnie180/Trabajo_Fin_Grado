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

Motor_DC::Motor_DC(uint8_t pinEnable, uint8_t pinA, uint8_t pinB, bool reverse)
{
    this->pinEnable = pinEnable;
    this->pinA = pinA;
    this->pinB = pinB;
    this->reverse = reverse;

    this->InitializatePins();
    this->ChangeSpeed(255);
    this->Stop();
}

void Motor_DC::setOffset(int8_t offset)
{
    this->offset = offset;
    this->ChangeSpeed(this->speed);
}

// Public
void Motor_DC::RotateRight()
{
    if (this->reverse)
    {
        digitalWrite(this->pinA, LOW);
        digitalWrite(this->pinB, HIGH);
    }
    else
    {
        digitalWrite(this->pinA, HIGH);
        digitalWrite(this->pinB, LOW);
    }
}

void Motor_DC::RotateLeft()
{
    if (this->reverse)
    {
        digitalWrite(this->pinA, HIGH);
        digitalWrite(this->pinB, LOW);
    }
    else
    {
        digitalWrite(this->pinA, LOW);
        digitalWrite(this->pinB, HIGH);
    }
}

void Motor_DC::Stop()
{
    digitalWrite(this->pinA, LOW);
    digitalWrite(this->pinB, LOW);
}

void Motor_DC::ChangeSpeed(uint8_t speed)
{
    this->speed = speed;
    int speedWithOffset = this->speed + offset;

    if (speedWithOffset < this->minSpeed){
        this->speed = this->minSpeed;
    } else if (speedWithOffset > this->maxSpeed){
        this->speed = this->maxSpeed;
    } else {
        this->speed = speedWithOffset;
    }

    analogWrite(this->pinEnable, this->speed);
}

void Motor_DC::setMinSpeed(uint8_t minSpeed){
    this->minSpeed = minSpeed;
}
void Motor_DC::setMaxSpeed(uint8_t maxSpeed){
    this->maxSpeed = maxSpeed;
}

uint8_t Motor_DC::GetMinSpeed(){
    return this->minSpeed;
}

uint8_t Motor_DC::GetMaxSpeed(){
    return this->maxSpeed;
}


// Private
void Motor_DC::InitializatePins()
{
    pinMode(this->pinEnable, OUTPUT);
    pinMode(this->pinA, OUTPUT);
    pinMode(this->pinB, OUTPUT);
}