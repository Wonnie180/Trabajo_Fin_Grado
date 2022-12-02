#ifndef _Led_H
#define _Led_H

#include "../ILed.hpp"
#include <Arduino.h>

class Led : public ILed{
    int led_pin;

public:    
    Led(int led_pin);
    void TurnOn();
    void TurnOff();
};

#endif