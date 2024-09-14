import math

def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma única raiz: {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: {x1} e {x2}")

# Exemplo de uso:
#resolver_equacao_segundo_grau(1, -3, 2)  # Exemplo: x² - 3x + 2 = 0