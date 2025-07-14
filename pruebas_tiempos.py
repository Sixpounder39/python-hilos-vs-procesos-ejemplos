# pruebas_tiempos.py
import time
import subprocess

resultados = []

# Realiza 10 pruebas de tiempo para comparar threading y multiprocessing
for i in range(10):
    # Aquí ejecuto los scripts de threading y multiprocessing
    inicio = time.time()
    subprocess.run(['python', 'threading_sumar.py'])
    tiempo_threading = time.time() - inicio

    inicio = time.time()
    subprocess.run(['python', 'multiprocessing_sumar.py'])
    tiempo_multiproc = time.time() - inicio

    # Almaceno los resultados
    resultados.append(f"Prueba {i+1}: Threading: {tiempo_threading:.2f}s, Multiprocessing: {tiempo_multiproc:.2f}s\n")

# Escribo los resultados en el archivo resultados.txt
with open('resultados.txt', 'w') as f:
    f.writelines(resultados)
