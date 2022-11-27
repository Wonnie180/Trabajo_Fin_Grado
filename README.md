<img src="Memoria/Bot-MindHive_Logo.svg" width="200">

# Trabajo_Fin_Grado
Repositorio para el TFG UPNA (2022/2023)


# Requisitos Previos
## Hardware
### Para cada robot
- ESP32
- 2x Motores
- Batería
- 74HC595N
- L293D
  
###
## Software
## Windows
### Programas necesarios
- [Visual Studio Community 2019](https://visualstudio.microsoft.com/es/vs/older-downloads/)
- [Cuda ToolKit](https://developer.nvidia.com/cuda-toolkit)
- [CMake](https://cmake.org/download/)
- [Anaconda3](https://www.anaconda.com/products/distribution)
- [Código fuente de OpenCV](https://github.com/opencv/opencv)
- [Código fuente de OpenCV Contrib](https://github.com/opencv/opencv_contrib) (Misma versión que OpenCV)


### Configuraciones
#### Entorno Python
Modulos a instalar:
> pip install pybluez2 ndarray-listener-2.0.1 aioconsole

#### Compilar OpenCV con soporte para CUDA (GPU)
Importante:
Durante el tutorial se va a asumir que el directorio donde se va a trabajar es la siguiente:
>C:/Users/Usuario/Escritorio/OpenCV-GPU

1.  Crea una carpeta donde se almacenara el código fuente de OpenCV
Por Ejemplo: 
>C:/Users/Usuario/Escritorio/OpenCV-GPU

2.  Descomprime tanto el código fuente de OpenCV como OpenCV Contrib en dicha carpeta.
Deberían aparecer dos nuevas carpetas de forma que la estructura quede de la siguiente forma:
>C:/Users/Usuario/Escritorio/OpenCV-GPU/opencv-4.6.0\
>C:/Users/Usuario/Escritorio/OpenCV-GPU/opencv_contrib-4.6.0

3.  Crea una carpeta llamada build en el directorio de trabajo.
>C:/Users/Usuario/Escritorio/OpenCV-GPU

4.  Abre CMake
    1. En el apartado "Where is the source code:" introduce la carpeta donde se ha descomprimido el código fuente de OpenCV  
    > C:/Users/Usuario/Escritorio/OpenCV-GPU/opencv-4.6.0

    2. En el apartado "Where to build the binaries:", introduce la carpeta build creada en el paso anterior .
    >C:/Users/Usuario/Escritorio/OpenCV-GPU/build

    3. Dale al botón __Configure__
        1. En el primer apartado selecciona Visual Studio 17 2022
        2. En el segundo apartado selecciona x64
        3. Deja el resto como viene y dale a __Finish__

    4. Ahora busca las siguientes opciones y marcalas:
        * WITH_CUDA
        * ENABLE_FAST_MATH
        * BUILD_opencv_world
        * CUDA_FAST_MATH
    
    5. Busca __OPENCV_EXTRA_MODULES_PATH__ e introduce la carpeta modules que esta en la carpeta de OpenCV Contrib
    >C:/Users/Usuario/Escritorio/opencv_contrib-4.6.0/modules

    6. Vuelve a pinchar en __Configure__. Si no da ningún error, procede al siguiente punto.

    7. Ahora busca __CUDA_ARCH_BIN__. Aquí hay que seleccionar la Arquitectura de tu gráfica NVIDIA. Para ello tendrás que ir a la [Wikipedia](https://en.wikipedia.org/wiki/CUDA) y buscar tu gráfica. Tras encontrarla en la tabla, Introduce la versión de la primera columna (6.1 en el caso de una GTX 1080ti por ejemplo) en el parametro de CMake.     
    8. Busca el parametro __CMAKE_CONFIGURATION_TYPES__ y deja solo "Release".
    9. Por último, presiona el botón __Generate__.

5. A continuación, abre una ventana de linea de comandos (cmd o Powershell) y ejecuta el siguiente comando:
> & 'C:\Program Files\CMake\bin\cmake.exe' --build "C:/Users/Usuario/Escritorio/OpenCV-GPU/build" --target INSTALL --config Release

6. Cuando el proceso de compilación termine, en la misma terminal ejecuta __Python__ y ejecuta el siguiente código:
```
import cv2
cv2.cuda.getCudaEnabledDeviceCount()
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Si el resultado es un número mayor que 0, ya está todo listo para utilizar CUDA con OpenCV.  

#### Linux
TBD