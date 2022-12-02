#ifndef _ILed_H
#define _ILed_H

class ILed
{

public:
    virtual ~ILed() = default;
    virtual void TurnOn() = 0;
    virtual void TurnOff() = 0;

protected:
    bool is_on;
};

#endif