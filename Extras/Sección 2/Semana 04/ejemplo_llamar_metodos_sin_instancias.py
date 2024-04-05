# Parte 1: Definimos la clase Persona
class Persona:
    '''
    Representa a una Persona, la cual tiene nombre y edad.
    - Cada vez que se instancia una persona,
      se agrega su nombre al set de nombres usados.
    - Estas personas pueden cumplir años y así aumentar su edad.
    '''
    nombres_usados = set()

    def __init__(self, nombre:str, edad:int) -> None:
        Persona.nombres_usados.add(nombre)
        self.nombre = nombre
        self.edad = edad

    def cumplir_años(self) -> None:
        self.edad += 1


# Parte 2: Definimos dos clases que eran de Persona.
# Ambas tienen el método saludas, pero la diferencia es que
# una necesita del 'self' para saludar y la otra no.
class PersonaSinStaticMethod(Persona):
    def saludar(self) -> None:
        '''
        Función que necesita del 'self' para saludar
        '''
        print('Hola')


class PersonaConStaticMethod(Persona):
    @staticmethod
    def saludar() -> None:
        '''
        Función que no necesita del 'self'
        '''
        print('Hola')


if __name__ == '__main__':
    # Parte 3: A partir de lo anterior, podemos instanciar Personas
    # y con ello acceder a sus atributos y sus métodos
    persona1 = PersonaSinStaticMethod('Ana', 10)
    persona1.saludar()
    print(f'Información original:    {persona1.nombre}, {persona1.edad} años')
    persona1.cumplir_años()
    print(f'Información actualizada: {persona1.nombre}, {persona1.edad} años')

    print('-' * 40)

    persona2 = PersonaConStaticMethod('Belén', 15)
    persona2.saludar()
    print(f'Información original:    {persona2.nombre}, {persona2.edad} años')
    persona2.cumplir_años()
    print(f'Información actualizada: {persona2.nombre}, {persona2.edad} años')

    print('-' * 40)

    # Parte 4: Pero en ocasiones surge la duda
    # P: ¿Necesito instancias a una clase para acceder a los atributos y métodos?
    # R: ¡Depende! Para todo lo que este relacionado al 'self' necesitaremos una
    #    instancia, pero si no hace uso del 'self' (como los atributos de clase o lo métodos estáticos),
    #    entonces podremos acceder a ellos sin tener que instanciar un objeto.
    print(f'Nombres usados: {PersonaConStaticMethod.nombres_usados}')
    PersonaConStaticMethod.saludar()
