from multiprocessing import Process
import time  # Para medir el tiempo de ejecución

# Esta función realiza una tarea intensiva en CPU: sumar muchas veces
def sumar():
    total = 0
    for _ in range(50_000_000):  # 50 millones de sumas
        total += 1

# Este bloque asegura que el código solo se ejecute si este archivo es el principal
if __name__ == "__main__":

    inicio = time.time()  # Marcamos el tiempo de inicio

    procesos = []  # Lista para guardar los procesos

    # Creamos y lanzamos 4 procesos independientes que ejecutan 'sumar'
    for _ in range(4):
        p = Process(target=sumar)  # Creamos un proceso
        p.start()  # Lo iniciamos
        procesos.append(p)  # Lo guardamos en la lista

    # Esperamos a que todos los procesos terminen su ejecución
    for p in procesos:
        p.join()  # join() bloquea hasta que el proceso finalice

    # Mostramos cuánto tiempo tomó ejecutar todas las tareas
    print(f"[multiprocessing] Tiempo total: {time.time() - inicio:.2f} segundos")
