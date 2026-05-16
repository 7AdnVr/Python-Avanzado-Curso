import time

def medir_tiempo_ejecucion(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        fin = time.perf_counter() 
        
        tiempo_total = fin - inicio
        print(f"El tiempo de ejecución fue de: {tiempo_total} segundos.")
        
        return resultado
    
    return envoltura

@medir_tiempo_ejecucion
def funcion_pesada():
    print("Generando 1 millón de números...")
    numeros = [i for i in range(1000000)]
    return numeros

print("--- Probando Ejercicio 5 ---")
lista_resultado = funcion_pesada()
print(f"Listo. La lista se generó con {len(lista_resultado)} elementos.\n")