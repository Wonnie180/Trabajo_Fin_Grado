#ifndef _Tropa_H
#define _Tropa_H

#include "../ITropa.hpp"

class Tropa : public ITropa{

public:
    Tropa(uint8_t id, ILed &_led, IMotor &_left_motor, IMotor &_right_motor);
    void Move_Forward();
    void Move_Backwards();
    void Turn_Left();
    void Turn_Right();
    void Change_Color(uint8_t R, uint8_t G, uint8_t B);        
};

#endif