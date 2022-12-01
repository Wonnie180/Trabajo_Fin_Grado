#ifndef _Motor_DC_H
#define _Motor_DC_H

#include <Arduino.h>

class Motor_DC {
    uint8_t pin_enable;
    uint8_t pin_1;
    uint8_t pin_2;
    uint8_t pwm;
    void InitializatePins();
public:    
    Motor_DC(uint8_t pin_enable, uint8_t pin_1, uint8_t pin_2);
    void RotateRight();
    void RotateLeft();
    void Stop();
    void ChangePWM(uint8_t pwm);
};

#endif