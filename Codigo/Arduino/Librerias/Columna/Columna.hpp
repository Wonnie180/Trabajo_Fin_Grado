/*
|| @file Columna.hpp
|| @version 1.0
|| @author Luis Jose Llamas Perez
|| @contact llamas.120781@e.unavarra.es
||
|| @description
|| | Columna class provides an abstract definition of a macro
|| #
||
|| @license
|| #
||
*/

#ifndef COLUMNA_H
#define COLUMNA_H

#define RW_T0 0x53
#define LOAD 0
#define SAVE 1
#define pin1_fila 18
#define pin1_col 2
#define LEDS_PIN 8
#define SD_PIN 9
#define finTransmision 4

#define byte unsigned char

class Columna {
   public:
    Columna(byte ID, byte ROWS, byte COLS);
    void inicializarWD();
    void escanearTeclado();
    void interpretarComando();

   private:
    // Manipulación de leds
    void setEstadoLed(byte Tecla, bool estado);

    // Variables
    enum WhatToSave {
        MACRO,
        STRING,
        INTENSIDAD,
        RGB_LED,
        LED,
        TOGGLES,
        MOS,
        PERFILCONF,
        PERFIL
    };
    byte id, nkeys, SD_or_Not, macroTeclas[12], intensidad, TeclaoString,
        *rowPins, *colPins, *estadoLeds, **toggleLeds_f, **macros;
    char *keys, macroString[120], *p_macroString;    
};
#endif

/*
|| @changelog
|| | 1.0 2019-06-03 - Luis Jose : Initial Release
|| #
*/
