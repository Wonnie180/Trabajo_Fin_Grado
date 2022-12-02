#ifndef _ITropa_H
#define _ITropa_H

#include <Arduino.h>
#include "../Motor/IMotor.hpp"
#include "../Led/ILed.hpp"

class ITropa
{
protected:
    ILed &led;
    IMotor &leftMotor;
    IMotor &rightMotor;

private:
    bool isMoving;
    uint8_t id;

public:
    virtual ~ITropa() = default;
    ITropa(uint8_t id, ILed &_led, IMotor &_leftMotor, IMotor &_rightMotor) : 
    led(_led), leftMotor(_leftMotor), rightMotor(_rightMotor)
    {
        this->id = id;
    }
    virtual void Move_Forward() = 0;
    virtual void Move_Backwards() = 0;
    virtual void Turn_Left() = 0;
    virtual void Turn_Right() = 0;
    virtual void Change_Color(uint8_t R, uint8_t G, uint8_t B) = 0;


};

#endif