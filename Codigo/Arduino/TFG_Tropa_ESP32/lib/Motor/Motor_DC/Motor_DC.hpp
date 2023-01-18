#ifndef _Motor_DC_H
#define _Motor_DC_H

#include <Arduino.h>
#include "../IMotor.hpp"

class Motor_DC : public IMotor{
private:

    uint8_t pinEnable;
    bool reverse = false;
    int offset = 0;
    uint8_t pinA;
    uint8_t pinB;

    void InitializatePins();

public:
    uint8_t minSpeed = 1;
    uint8_t maxSpeed = 255;

    Motor_DC(uint8_t pinEnable, uint8_t pinA, uint8_t pinB);
    Motor_DC(uint8_t pinEnable, uint8_t pinA, uint8_t pinB, bool reverse);
    void setOffset(int8_t offset);
    void RotateRight();
    void RotateLeft();
    void Stop();
    void ChangeSpeed(uint8_t speed);
    uint8_t GetMinSpeed();
    uint8_t GetMaxSpeed();
    void setMinSpeed(uint8_t minSpeed);
    void setMaxSpeed(uint8_t maxSpeed);

};

#endif