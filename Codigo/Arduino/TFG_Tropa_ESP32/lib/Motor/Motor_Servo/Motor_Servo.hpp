#ifndef _Motor_Servo_H
#define _Motor_Servo_H

#include <Arduino.h>
#include "../IMotor.hpp"
#include <ESP32Servo.h>

class Motor_Servo : public IMotor{
    uint8_t pinControl;
    bool reverse = false;
    int8_t offset = 0;
    uint8_t speed = 1;
    //Servo motor;
    void InitializatePins();
public:
    Servo motor;
    Motor_Servo(uint8_t pinControl);
    Motor_Servo(uint8_t pinControl, bool reverse);
    void setOffset(int8_t offset);
    void RotateRight();
    void RotateLeft();
    void Stop();
    void ChangeSpeed(uint8_t speed);
};

#endif