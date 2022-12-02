#include "Tropa.hpp"

// Constructor
Tropa::Tropa(uint8_t id, ILed &_led, IMotor &_left_motor, IMotor &_right_motor) : ITropa(id, _led, _left_motor, _right_motor)
{

}

// Public
void Tropa::Move_Forward()
{
}

void Tropa::Move_Backwards()
{
}

void Tropa::Turn_Left()
{
}

void Tropa::Turn_Right()
{
}

void Tropa::Change_Color(uint8_t R, uint8_t G, uint8_t B)
{
    if (R == 0){
        this->led.TurnOff();
    } else {
        this->led.TurnOn();
    }

}

// Private