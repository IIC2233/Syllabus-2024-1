# Al momento de trabajar con estructuras que se pueden desempaquetar,
# como listas, tuplas y diccionarios
lista = [1, 2, 3, 4, 5, 6, 7]
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Podemos utilizar el operador * para desempaquetar la información de estas estructuras:
# (Los * y ** no solo se utilizan en la definición de clases y funciones)
print('Podemos desempaquetar:')
print('- El contenido de listas:        ', *lista)
print('- Las llaves de un diccionario:  ', *diccionario)
print('- Los valores de un diccionario: ', *diccionario.values())
print('- Los pares de un diccionario:   ', *diccionario.items())

# Podemos utilizar el operador ** en contextos donde se deba asociar un valor a una llave.
# Por ejemplo, cuando usamos strings y format:
print('- En textos que usan format:      {a} {c} {a} {b}'.format(**diccionario))
