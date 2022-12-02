#include "WS2818B.hpp"

WS2818B::WS2818B(uint8_t led_pin)
{
    this->ledPin = ledPin;
    this->is_on = false;
    pinMode(this->ledPin, OUTPUT);
}

// Public
void WS2818B::TurnOn()
{
    this->is_on = true;
    digitalWrite(this->ledPin, HIGH);
}

void WS2818B::TurnOff()
{
    this->is_on = false;
    digitalWrite(this->ledPin, LOW);
}

void WS2818B::ChangeColor(uint8_t R, uint8_t G, uint8_t B){
    this->R = R;
    this->G = G;
    this->B = B;
    // digitalwrite blablabla
}

