#ifndef _Led_RGB_H
#define _Led_RGB_H

#include <Arduino.h>
#include "../ILed_RGB.hpp"
class WS2818B : public ILed_RGB
{
    uint8_t ledPin;

public:
    WS2818B(uint8_t ledPin);
    void TurnOn();
    void TurnOff();
    void ChangeColor(uint8_t R, uint8_t G, uint8_t B);
};

#endif