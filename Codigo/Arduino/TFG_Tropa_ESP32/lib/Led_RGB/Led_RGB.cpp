#include "Led_RGB.hpp"

Led_RGB::Led_RGB(uint8_t led_pin)
{
    this->led_pin = led_pin;
    this->is_on = false;
    pinMode(this->led_pin, OUTPUT);
}

// Public
void Led_RGB::TurnOn()
{
    this->is_on = true;
    digitalWrite(this->led_pin, HIGH);
}

void Led_RGB::TurnOff()
{
    this->is_on = false;
    digitalWrite(this->led_pin, LOW);
}

void Led_RGB::TurnOnOff()
{
    if (this->is_on)
        this->TurnOff();
    else
        this->TurnOn();
}

void Led_RGB::SetColor(uint8_t RGB[]){
    this->RGB[0] = RGB[0];
    this->RGB[1] = RGB[1];
    this->RGB[2] = RGB[2];
}

void Led_RGB::ChangeColor(){
    // digitalwrite blablabla    
}

