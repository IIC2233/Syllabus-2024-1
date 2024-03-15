import dcciudad

##############################
#####    Imprimir red    #####
##############################

print("imprimir_red - Ejemplo 1\n")
red_1 = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
estaciones_1 = ["A", "B", "C", "D"]

dcciudad.imprimir_red(red_1, estaciones_1)

print("\nimprimir_red - Ejemplo 2\n")
red_2 = [
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
]


estaciones_2 = [
    "Shibuya",
    "Shinjuku",
    "Tokyo",
    "Ikebukuro",
    "Ueno",
    "Ginza",
    "Harajuku",
    "Akihabara",
    "Roppongi",
    "Odaiba-kaihinkoen",
    "Hamamatsucho"
]

dcciudad.imprimir_red(red_2, estaciones_2)

for i in range(3):
    print("-"*50)
##############################
#####   Elevar Matriz    #####
##############################
red = [
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
print("elevar_matriz - red original")
for x in red:
    print(x)

print("\nelevar_matriz - elevar a 2")
red_elevada_2 = dcciudad.elevar_matriz(red, 2)
for x in red_elevada_2:
    print(x)

print("\nelevar_matriz - elevar a 3")
red_elevada_3 = dcciudad.elevar_matriz(red, 3)
for x in red_elevada_3:
    print(x)

print("\nelevar_matriz - elevar a 4")
red_elevada_4 = dcciudad.elevar_matriz(red, 4)
for x in red_elevada_4:
    print(x)
print()

for i in range(3):
    print("-"*50)
##############################
#####     Alcanzable     #####
##############################


red = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
"""
Estacion 0 -> Estacion 1
Estacion 1 -> Estacion 2 y Estacion 3
Estacion 2 -> Estacion 3
Estacion 3 -> sin conexiones
"""

print("alcanzable - ejemplo 1 (existe camino desde 0 a 3)")
inicio = 0
destino = 3

resultado = dcciudad.alcanzable(red, inicio, destino)
print(f"Existe camino desde {inicio} hasta {destino}: {resultado}")

print("\nalcanzable - ejemplo 2 (no existe camino desde 3 a 0)")
inicio = 3
destino = 0

resultado = dcciudad.alcanzable(red, inicio, destino)
print(f"Existe camino desde {inicio} hasta {destino}: {resultado}")