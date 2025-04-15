# Algoritmo Genético para Optimización de Inventario

Este proyecto implementa un algoritmo genético para optimizar la selección de productos en un inventario con restricciones de peso y maximización de beneficios.

## Descripción

El algoritmo genético resuelve un problema de optimización donde se debe seleccionar la cantidad óptima de 7 diferentes productos mágicos, considerando:
- Restricción de peso máximo (30 unidades)
- Maximización del beneficio total
- Restricciones específicas para algunos productos

### Productos Disponibles
- Decoy Detonators
- Love Potion 
- Extendable Ears
- Skivin Snackbox
- Fever Fudge
- Puking Pastilles
- Nosebleed Nougat

## Características

- Implementación de selección por ruleta
- Cruce de cromosomas con probabilidad de 0.85
- Mutación con probabilidad de 0.1
- Evaluación de aptitud basada en precio total
- Restricciones de peso para mantener soluciones válidas

## Requisitos

```python
import numpy as np
```

## Uso

Para ejecutar el algoritmo:

```python
python main.py
```

El programa mostrará:
- El cromosoma más apto (mejor solución encontrada)
- Precio total alcanzado
- Desglose de cantidades por producto

## Parámetros del Algoritmo

- Número de cromosomas: 10
- Generaciones: 50
- Probabilidad de cruce (Pc): 0.85
- Probabilidad de mutación (Pm): 0.1
- Umbral de cruce: 0.5

