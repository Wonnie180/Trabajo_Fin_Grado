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

protected:
    uint8_t speed;
};

#endif