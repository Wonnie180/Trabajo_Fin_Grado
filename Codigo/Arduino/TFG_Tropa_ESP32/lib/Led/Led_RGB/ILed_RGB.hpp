#ifndef _ILed_RGB_H
#define _ILed_RGB_H

#include "../ILed.hpp"
#include <Arduino.h>

class ILed_RGB : public ILed
{

public:
    virtual ~ILed_RGB() = default;
    virtual void ChangeColor(uint8_t R, uint8_t G, uint8_t B) = 0;

protected:
    uint8_t R;
    uint8_t G;
    uint8_t B;
};

#endif