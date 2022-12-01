#ifndef _Led_H
#define _Led_H

#include <Arduino.h>

class Led {
    int led_pin;
    bool is_on;

public:    
    Led(int led_pin);
    void TurnOn();
    void TurnOff();
};

#endif