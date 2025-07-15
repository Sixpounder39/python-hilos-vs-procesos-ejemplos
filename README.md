# python-hilos-vs-procesos-ejemplos

Ejemplos y comparativas para entender el GIL, concurrencia y paralelismo en Python.

# 🐍 Concurrencia, Paralelismo y el GIL en Python

Este repositorio contiene ejemplos prácticos, explicaciones y comparativas para entender cómo funciona la **concurrencia y el paralelismo** en Python, y cómo el **GIL (Global Interpreter Lock)** impacta en la ejecución de programas multihilo.

## 🎯 Objetivo

Ayudar a estudiantes y desarrolladores a entender:
- Qué es el GIL y por qué existe
- Cuándo usar `threading` y cuándo `multiprocessing`
- Cómo medir el rendimiento de ambos enfoques

---

## 📚 Contenido

| Archivo                  | Descripción                                                       |
|--------------------------|-------------------------------------------------------------------|
| `threading_sumar.py`     | Ejemplo que usa hilos (`threading`) para ejecutar una tarea CPU-intensiva. |
| `multiprocessing_sumar.py` | Ejemplo que usa procesos (`multiprocessing`) para la misma tarea, logrando paralelismo real. |
| `pruebas_tiempos.py`     | Ejecuta múltiples pruebas con ambos scripts y guarda los resultados en `resultados.txt`. |
| `resultados.txt`         | Archivo con los tiempos de ejecución guardados tras correr las pruebas. |
| `LICENSE`                | Licencia MIT para este proyecto.                                 |

---

## 🚀 Cómo ejecutar los ejemplos

### Requisitos
Python 3.9 o superior (se ha probado con Python 3.11)

## 💻 Detalles del equipo de pruebas

Las pruebas de rendimiento se realizaron en un equipo con las siguientes características:

- Procesador: AMD Ryzen 5 4600H with Radeon Graphics, 3000 MHz  
- Núcleos físicos: 6  
- Núcleos lógicos (hilos): 12  
- Disco: Unidad de estado sólido (SSD)  
- Memoria RAM: 32 GB  

Ten en cuenta que los tiempos de ejecución pueden variar según el hardware y la carga del sistema.

## 📚 Recursos adicionales

Para complementar estos ejemplos y entender mejor los conceptos, te invito a leer mis posts en LinkedIn:

- [Conceptos básicos de concurrencia en Python](https://www.linkedin.com/posts/luis-armando-escobar-macias_conceptos-b%C3%A1sicos-de-concurrencia-python-activity-7345287962625986560-seNb?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFo-20EB4H4UhACd3la_z-EK0Vhy5f1Y6zE)  
    Una introducción clara y sencilla para entender qué es la concurrencia y paralelismo en Python.

- [Global Interpreter Lock (GIL) en Python: ¿qué es y por qué importa?](https://www.linkedin.com/posts/luis-armando-escobar-macias_gil-python-activity-7350902040115458048-ckmc?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFo-20EB4H4UhACd3la_z-EK0Vhy5f1Y6zE)  
    Explicación del GIL de Python

Estos posts explican los conceptos con analogías y ejemplos para hacer el aprendizaje más fácil y ameno.