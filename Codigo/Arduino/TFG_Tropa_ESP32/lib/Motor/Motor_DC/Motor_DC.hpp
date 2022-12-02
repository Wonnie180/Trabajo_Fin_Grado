#ifndef _Motor_DC_H
#define _Motor_DC_H

#include <Arduino.h>
#include "../IMotor.hpp"

class Motor_DC : public IMotor{
    uint8_t pinEnable;
    uint8_t pinA;
    uint8_t pinB;
    void InitializatePins();
public:    
    Motor_DC(uint8_t pinEnable, uint8_t pinA, uint8_t pinB);
    void RotateRight();
    void RotateLeft();
    void Stop();
    void ChangeSpeed(uint8_t speed);
};

#endif