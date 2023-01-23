#include "Tropa.hpp"

// Constructor
Tropa::Tropa(uint8_t id, ILed &_led, IMotor &_left_motor, IMotor &_right_motor) : ITropa(id, _led, _left_motor, _right_motor)
{
}

// Public
void Tropa::Move_Forward()
{
    // this->leftMotor.ChangeSpeed(this->leftMotor.GetMaxSpeed());
    // this->rightMotor.ChangeSpeed(this->rightMotor.GetMaxSpeed());
    this->leftMotor.ChangeSpeed(this->maxSpeed);
    this->rightMotor.ChangeSpeed(this->maxSpeed);

    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateRight();
        this->rightMotor.RotateLeft();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Move_Backwards()
{    
    this->leftMotor.ChangeSpeed(this->maxSpeed);
    this->rightMotor.ChangeSpeed(this->maxSpeed);

    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateLeft();
        this->rightMotor.RotateRight();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Turn_Left()
{
    this->leftMotor.ChangeSpeed(this->middleSpeed);
    this->rightMotor.ChangeSpeed(this->maxSpeed);

    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateRight();
        this->rightMotor.RotateLeft();
    }
    this->leftMotor.Stop();
    this->rightMotor.Stop();
}

void Tropa::Turn_Right()
{
    this->leftMotor.ChangeSpeed(this->maxSpeed);
    this->rightMotor.ChangeSpeed(this->middleSpeed);

    unsigned long timeEnd = millis() + this->actionDelay;

    while (millis() < timeEnd)
    {
        this->leftMotor.RotateRight();
        this->rightMotor.RotateLeft();
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
void Tropa::Set_MaxMiddleMinSpeeds(uint8_t max, uint8_t mid, uint8_t min)
{
    this->maxSpeed = max;
    this->middleSpeed = mid;
    this->minSpeed = min;
}