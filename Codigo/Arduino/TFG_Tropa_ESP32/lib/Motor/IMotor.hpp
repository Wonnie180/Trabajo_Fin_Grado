#ifndef _IMotor_H
#define _IMotor_H


class IMotor
{

public:
    virtual ~IMotor() = default;
    virtual void RotateRight() = 0;
    virtual void RotateLeft() = 0;
    virtual void Stop() = 0;
    virtual void ChangeSpeed(uint8_t speed) = 0;
    virtual uint8_t GetMinSpeed() = 0;
    virtual uint8_t GetMaxSpeed() = 0;

protected:
    uint8_t speed = 255;
    uint8_t minSpeed = 1;
    uint8_t maxSpeed = 255;
};

#endif