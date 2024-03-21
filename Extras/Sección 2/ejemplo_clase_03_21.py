def función_mala(lista: list = []) -> None:
    '''
    Función que recibe una lista.
    Le agrega a dicha lista el valor de su largo y la imprime.

    Si no recibe una lista, usará la misma lista por defecto
    en los llamados de la función.
    '''
    lista.append(len(lista))
    print(lista)


def función_buena(lista: list | None = None) -> None:
    '''
    Función que recibe una lista.
    Le agrega a dicha lista el valor de su largo y la imprime.
    
    Si no recibe una lista, creará una instancia distinta de
    lista en los llamados de la función.
    '''
    if lista is None:
        lista = []

    lista.append(len(lista))
    print(lista)


if __name__ == '__main__':
    print('Ejecución usando la función mala')
    función_mala(['a', 'b'])
    función_mala()
    función_mala()
    función_mala()

    print('\nEjecución usando la función buena')
    función_buena(['a', 'b'])
    función_buena()
    función_buena()
    función_buena()
