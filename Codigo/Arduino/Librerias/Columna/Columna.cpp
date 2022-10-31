/*
|| @file Columna.cpp
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

// default constructor
#include "./Columna.hpp"

Columna::Columna(byte ID, byte ROWS, byte COLS)
{
    id = ID;
    nkeys = ROWS * COLS;  
}

void Columna::inicializarWD()
{    
}

/*
|| @changelog
|| | 1.0 2019-06-03 - Luis Jose : Initial Release
|| #
*/
