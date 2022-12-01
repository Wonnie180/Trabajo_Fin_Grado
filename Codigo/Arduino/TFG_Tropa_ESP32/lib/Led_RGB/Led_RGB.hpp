#ifndef _Led_RGB_H
#define _Led_RGB_H

#include <Arduino.h>

class Led_RGB
{
    uint8_t led_pin;
    uint8_t RGB[3];
    bool is_on;

public:
    Led_RGB(uint8_t led_pin);
    void TurnOn();
    void TurnOff();
    void TurnOnOff();
    void SetColor(uint8_t RGB[]);
    void ChangeColor();
};

#endif