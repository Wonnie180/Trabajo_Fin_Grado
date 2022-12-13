#include "Tropa.hpp"

// Constructor
Tropa::Tropa(uint8_t id, ILed &_led, IMotor &_left_motor, IMotor &_right_motor) : ITropa(id, _led, _left_motor, _right_motor)
{
}

// Public
void Tropa::Move_Forward()
{
    this->leftMotor.ChangeSpeed(this->fullSpeed);
    this->rightMotor.ChangeSpeed(this->fullSpeed);

    unsigned long timeEnd = millis() + this->actionDelay;

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
    this->leftMotor.ChangeSpeed(this->fullSpeed);
    this->rightMotor.ChangeSpeed(this->fullSpeed);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + this->actionDelay;

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
    this->leftMotor.ChangeSpeed(this->reducedSpeed);
    this->rightMotor.ChangeSpeed(this->fullSpeed);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Turn_Right()
{
    this->leftMotor.ChangeSpeed(this->fullSpeed);
    this->rightMotor.ChangeSpeed(this->reducedSpeed);

    unsigned long time = 1000;
    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
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