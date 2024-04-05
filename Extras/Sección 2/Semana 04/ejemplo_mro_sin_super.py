def print_clase_atributos(clase=None, atributos=None) -> None:
    '''
    Función que recibe la información de una clase (Nombre, atributos, args, kwargs)
    y lo imprime en un formato en específico
    '''
    platilla_texto = '{:<15} | {:<15} | {:<15} | {}'
    if not (clase and atributos):
        print(platilla_texto.format('Nombre', 'Atributo Input', '*args', '**kwargs'))
        print('-' * 100)
    else:
        print(platilla_texto.format(clase, atributos[0], repr(atributos[1]), repr(atributos[2])))


class ClaseAbuelo:
    def __init__(self, atributo3, *args, **kwargs):
        print_clase_atributos('ClaseAbuelo', (atributo3, args, kwargs))
        self.atributo3 = atributo3


class ClasePadre(ClaseAbuelo):
    def __init__(self, atributo1, *args, **kwargs):
        print_clase_atributos('ClasePadre', (atributo1, args, kwargs))
        self.atributo1 = atributo1
        ClaseAbuelo.__init__(self, *args, **kwargs)


class ClaseMadre(ClaseAbuelo):
    def __init__(self, atributo2, *args, **kwargs):
        print_clase_atributos('ClaseMadre', (atributo2, args, kwargs))
        self.atributo2 = atributo2
        ClaseAbuelo.__init__(self, *args, **kwargs)


class ClaseHija(ClasePadre, ClaseMadre):
    def __init__(self, atributo1, atributo2, atributo3):
        print_clase_atributos('ClaseHija', (f'{atributo1}, {atributo2}, {atributo3}', '-', '-'))
        ClasePadre.__init__(self, atributo1, atributo3)
        ClaseMadre.__init__(self, atributo2, atributo3)


if __name__ == '__main__':
    # Cuando no se hace uso de 'super()' para manejar la multi-herencia, 
    # el recorrido del MRO pasará 2 veces por la ClaseAbuelo.

    # Para verlo con mayor claridad, revisar el flujo que se muestra en
    # la presentación de la clase 4.

    print_clase_atributos()
    ClaseHija(1, 2, 3)
