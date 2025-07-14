import threading  # Importamos el módulo para trabajar con hilos (threads)
import time       # Para medir el tiempo de ejecución

# Esta función realiza una operación intensiva en CPU: sumar muchas veces
def sumar():
    total = 0
    for _ in range(50_000_000):  # 50 millones de sumas
        total += 1

inicio = time.time()  # Marcamos el tiempo de inicio

hilos = []  # Creamos una lista para guardar los hilos

# Lanzamos 4 hilos que ejecutarán la función 'sumar'
for _ in range(4):
    t = threading.Thread(target=sumar)  # Creamos un hilo que ejecuta 'sumar'
    t.start()  # Iniciamos el hilo
    hilos.append(t)  # Lo agregamos a la lista de hilos

# Esperamos a que todos los hilos terminen su trabajo
for t in hilos:
    t.join()  # join() bloquea hasta que el hilo termine

# Mostramos cuánto tiempo tardó todo el proceso
print(f"[threading] Tiempo total: {time.time() - inicio:.2f} segundos")
