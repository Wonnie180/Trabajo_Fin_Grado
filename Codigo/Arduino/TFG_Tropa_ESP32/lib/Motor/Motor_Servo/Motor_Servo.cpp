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
void Motor_Servo::setOffset(int8_t offset)
{
    this->offset = offset;
    this->ChangeSpeed(this->speed);
}

void Motor_Servo::RotateRight()
{
    this->motor.write(this->CalculateAngle(!this->reverse));
}

void Motor_Servo::RotateLeft()
{
    this->motor.write(this->CalculateAngle(this->reverse));
}

void Motor_Servo::Stop()
{
    this->motor.write(90);
}

void Motor_Servo::ChangeSpeed(uint8_t speed)
{
    this->speed = speed;
    int speedWithOffset = this->speed + offset;

    if (speedWithOffset < this->minSpeed)
    {
        this->speed = this->minSpeed;
    }
    else if (speedWithOffset > this->maxSpeed)
    {
        this->speed = this->maxSpeed;
    }
    else
    {
        this->speed = speedWithOffset;
    }
}

void Motor_Servo::setMinSpeed(uint8_t minSpeed)
{
    this->minSpeed = minSpeed;
}
void Motor_Servo::setMaxSpeed(uint8_t maxSpeed)
{
    this->maxSpeed = maxSpeed;
}

uint8_t Motor_Servo::GetMinSpeed()
{
    return this->minSpeed;
}

uint8_t Motor_Servo::GetMaxSpeed()
{
    return this->maxSpeed;
}

// Private
void Motor_Servo::InitializatePins()
{
    pinMode(this->pinControl, OUTPUT);
}

uint8_t Motor_Servo::CalculateAngle(bool right)
{
    uint8_t angle = 90;
    if ((right && this->reverse) || (!right && !this->reverse))
    {
        angle = map(this->speed,
                    this->minSpeed,
                    this->maxSpeed,
                    90, 0);
    }
    else
    {
        angle = map(this->speed,
                    this->minSpeed,
                    this->maxSpeed,
                    90, 180);
    }

    Serial.print("Angulo_Velocidad: ");
    Serial.print(angle);
    Serial.print(" | Min: ");
    Serial.print(this->minSpeed);
    Serial.print(" | Max: ");
    Serial.print(this->maxSpeed);
    Serial.print(" | Speed: ");
    Serial.println(this->speed);
    return angle;
}