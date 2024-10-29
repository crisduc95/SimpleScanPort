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

  ```bash
  pip install colorama
