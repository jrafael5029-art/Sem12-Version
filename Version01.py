import math 

DATASET = [
    ["Pare", 3, 1, 0],
    ["Límite 60", 1, 1, 60],
]

def reconocer_senal(entrada):
    mejor_senal = None
    menor_distancia = float("inf")
    for senal in DATASET:
        caracteristicas = senal[1:]
        distancia = math.sqrt(
            sum((a - b) ** 2
            for a, b in zip(entrada, caracteristicas))
        )
        if distancia < menor_distancia:
            menor_distancia = distancia
            mejor_senal = senal
    return mejor_senal, round(menor_distancia, 2) 

entradas_prueba = [
    [3, 1, 0],   # → Pare
    [1, 1, 60],  # → Límite 60
]

print("=============================================")
print("  RECONOCIMIENTO DE SEÑALES DE TRÁNSITO")
print("=============================================")

for entrada in entradas_prueba:
    senal, distancia = reconocer_senal(entrada)
    tipo = "Exacta" if distancia == 0.0 else "Aproximada"
    print(f"Entrada   : forma={entrada[0]}  color={entrada[1]}  velocidad={entrada[2]}")
    print(f"Reconocida: {senal[0]:<25} distancia={distancia}  ({tipo})")

print("=============================================")