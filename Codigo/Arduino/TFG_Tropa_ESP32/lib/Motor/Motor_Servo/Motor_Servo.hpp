#ifndef _Motor_Servo_H
#define _Motor_Servo_H

#include <Arduino.h>
#include "../IMotor.hpp"
#include <ESP32Servo.h>

class Motor_Servo : public IMotor{
private:
    Servo motor;
    uint8_t pinControl;
    bool reverse = false;
    int offset = 0;
    
    void InitializatePins();
    uint8_t CalculateAngle(bool right);

public:    
    Motor_Servo(uint8_t pinControl);
    Motor_Servo(uint8_t pinControl, bool reverse);
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