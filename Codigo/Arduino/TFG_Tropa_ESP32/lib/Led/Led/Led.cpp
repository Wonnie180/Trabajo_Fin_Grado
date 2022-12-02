#include "Led.hpp"

// Constructor
Led::Led(int led_pin)
{
    this->led_pin = led_pin;
    this->is_on = false;
    pinMode(this->led_pin, OUTPUT);
}

// Public
void Led::TurnOn()
{
    this->is_on = true;
    digitalWrite(this->led_pin, HIGH);
}

void Led::TurnOff()
{
    this->is_on = false;
    digitalWrite(this->led_pin, LOW);
}
