#ifndef _CommandEnum_H
#define _CommandEnum_H

#include <Arduino.h>

enum CommandEnum : uint8_t { 
    Forward = 0, 
    Backwards = 1, 
    Turn_Left = 2, 
    Turn_Right = 3,
    Change_Color = 4 
    };

#endif
