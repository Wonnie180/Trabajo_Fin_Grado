#include "Motor_Servo.hpp"

// Constructor
Motor_Servo::Motor_Servo(uint8_t pinControl)
{
    this->pinControl = pinControl;

    this->InitializatePins();

    this->motor.attach(pinControl);
    this->ChangeSpeed(255);
    this->Stop();
}

Motor_Servo::Motor_Servo(uint8_t pinControl, bool reverse)
{
    this->pinControl = pinControl;
    this->reverse = reverse;

    this->InitializatePins();

    this->motor.attach(pinControl);
    this->ChangeSpeed(255);
    this->Stop();
}



// Public
void Motor_Servo::setOffset(int8_t offset){
    this->offset = offset;
}

void Motor_Servo::RotateRight()
{
    if (this->reverse)
    {
        this->motor.write(80-this->offset);
    }
    else
    {
        this->motor.write(100+this->offset);
    }
}

void Motor_Servo::RotateLeft()
{
    if (this->reverse)
    {
        this->motor.write(100+this->offset);
    }
    else
    {
        this->motor.write(80-this->offset);
    }
}

void Motor_Servo::Stop()
{
    this->motor.write(90);
}

void Motor_Servo::ChangeSpeed(uint8_t speed)
{
    this->speed = speed;
}

// Private
void Motor_Servo::InitializatePins()
{
    pinMode(this->pinControl, OUTPUT);
}