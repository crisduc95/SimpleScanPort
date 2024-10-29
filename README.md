# Simple Port Scanner

Este proyecto es un escáner de puertos simple desarrollado en Python que utiliza la biblioteca `socket` para verificar si un puerto está abierto o cerrado en una dirección IP específica. El script permite escanear un solo puerto o un rango de puertos, y utiliza `colorama` para imprimir los resultados en colores.

## Estructura del Proyecto

- **scanhosts.py**: Contiene la clase `ScanHost` con métodos para escanear puertos TCP.
- **main.py**: Script principal que maneja los argumentos de la línea de comandos y ejecuta los métodos de escaneo.

## Requisitos

- **Python 3**
- **colorama**
- **argparse**
- **socket**

## OPCIONES
- **--t**: target
- **--p**: Rango de puertos.
- **--s**: single

## USO ESCANEO UN SOLO PUERTO
  ```bash
python3 main.py --t 192.168.1.1 --p 80 80 --single
 ```

## USO ESCANEO VARIOS PUERTOS
  ```bash
python3 main.py --t 192.168.1.1 --p 20 100

 ```

  
