#include "Tropa.hpp"

// Constructor
Tropa::Tropa(uint8_t id, ILed &_led, IMotor &_left_motor, IMotor &_right_motor) : ITropa(id, _led, _left_motor, _right_motor)
{
}

// Public
void Tropa::Move_Forward()
{
    this->leftMotor.ChangeSpeed(255);
    this->rightMotor.ChangeSpeed(255);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + time;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Move_Backwards()
{
    this->leftMotor.ChangeSpeed(255);
    this->rightMotor.ChangeSpeed(255);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + time;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateRight();
        this->rightMotor.RotateLeft();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Turn_Left()
{
    this->leftMotor.ChangeSpeed(128);
    this->rightMotor.ChangeSpeed(255);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + time;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
}

void Tropa::Turn_Right()
{
    this->leftMotor.ChangeSpeed(255);
    this->rightMotor.ChangeSpeed(128);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + time;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
}

void Tropa::Change_Color(uint8_t R, uint8_t G, uint8_t B)
{
    if ((R | G | B) == 0)
    {
        this->led.TurnOff();
    }
    else
    {
        this->led.TurnOn();
    }
}

// Private