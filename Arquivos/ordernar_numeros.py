import random

def bubble_sort(valores):
    n = len(valores)
    for i in range(n):
        for j in range(0, n-i-1):
            if valores[j] > valores[j+1]:
                valores[j], valores[j+1] = valores[j+1], valores[j]
    return valores

def ordenar_numeros(n):
    numeros = [random.randint(1, 100) for _ in range(n)]
    print(f"Números gerados: {numeros}")
    numeros_ordenados = bubble_sort(numeros)
    print(f"Números ordenados: {numeros_ordenados}")


ordenar_numeros(50)
