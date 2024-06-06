from abc import ABC, abstractmethod
import re
import requests

from constantes_cliente import REGEX_APELLIDO, REGEX_N_ALUMNO, REGEX_NOMBRE, SERVER_URL


###################################################################################
#                            COMANDOS API                                         #
###################################################################################

class Client(ABC):
    @abstractmethod
    def get_ayudantes_list():
        pass
    @abstractmethod
    def get_ayudante_by_id(id_ayudante: int):
        pass
    @abstractmethod
    def create_ayudante(nombre: str, apellido: str, n_alumno: str):
        pass
    @abstractmethod
    def fill_motivación(id_ayudante: int, motivacion: str):
        pass
    @abstractmethod
    def asignar_veredicto(id_ayudante: int, veredicto: str):
        pass


class ApiClient(Client):
    def get_ayudantes_list(self):
        res = requests.get(f"{SERVER_URL}/ayudantes")


        if res.ok:
            ayudantes = res.json()["Ayudantes"]
            return ayudantes
        return None

    def get_ayudante_by_id(self, id_ayudante: int):
        res = requests.get(f"{SERVER_URL}/ayudantes/{id_ayudante}")

        if res.ok:
            return res.json()["Ayudante"]
        return None

    def create_ayudante(self, nombre: str, apellido: str, n_alumno: str):
        headers = {
            "content-type": "application/json"
        }

        body = {
            "nombre": nombre,
            "apellido": apellido,
            "n_alumno": n_alumno
        }

        res = requests.post(f"{SERVER_URL}/ayudantes", headers=headers, json=body)

        if res.ok:
            return res.json()["Ayudante"]
        return None

    def fill_motivación(self, id_ayudante: int, motivacion: str):
        headers = {
            "content-type": "application/json"
        }

        body = {
            "motivacion": motivacion
        }

        res = requests.post(f"{SERVER_URL}/ayudantes/{id_ayudante}/motivacion", headers=headers, json=body)

        if res.ok:
            return res.json()["Ayudante"]
        return None

    def asignar_veredicto(self, id_ayudante: int, veredicto: str):
        res = requests.post(f"{SERVER_URL}/ayudantes/{id_ayudante}/veredicto?estado={veredicto}")

        if res.ok:
            return res.json()["Ayudante"]
        return None

###################################################################################
#                                MOCKS                                            #
###################################################################################

class MockClient(Client):
    def __init__(self):
        self.ayudantes = [
            {
                "id": 1,
                "nombre": "Julio",
                "apellido": "Huerta",
                "n_alumno": "20544407",
                "estado": "rechazado",
                "motivacion" : "ser admin"
            },
            {
                "id": 2,
                "nombre": "Julián",
                "apellido": "García",
                "n_alumno": "18638279",
                "estado": "aceptado",
                "motivacion" : "dominar el mundo"
            }
        ]

    def get_ayudantes_list(self):
        return self.ayudantes

    def get_ayudante_by_id(self, id_ayudante: int):
        return next(ayudante for ayudante in self.ayudantes if ayudante["id"] == id_ayudante)

    def create_ayudante(self, nombre: str, apellido: str, n_alumno: str):
        ayudante = {
            "id": max(ayudante["id"] for ayudante in self.ayudantes) + 1,
            "nombre": nombre,
            "apellido": apellido,
            "n_alumno": n_alumno,
            "estado": "pendiente",
            "motivacion" : ""
        }
        self.ayudantes.append(ayudante)

        return ayudante

    def fill_motivación(self, id_ayudante: int, motivacion: str):
        ayudante = next(ayudante for ayudante in self.ayudantes if ayudante["id"] == id_ayudante)
        ayudante["motivacion"] = motivacion

        return ayudante

    def asignar_veredicto(self, id_ayudante: int, veredicto: str):
        ayudante = next(ayudante for ayudante in self.ayudantes if ayudante["id"] == id_ayudante)

        ayudante["estado"] = veredicto

        return ayudante
        
###################################################################################
#                                     REGEX                                       #
###################################################################################

def revisar_regex(regex, string):
   return bool(re.search(regex, string))

###################################################################################
#                           INTERFAZ POR CONSOLA                                  #
###################################################################################


class Menus:
    principal = 0
    salir = 1
    lista_ayudantes = 2
    detalles_ayudante = 3
    crear_ayudante = 4
    ingresar_motivacion = 5
    asignar_veredicto = 6


client = ApiClient()

def regex_input(regex, prompt="Ingrese su input: "):
    while True:
        i = input(prompt).strip()
        if not revisar_regex(regex, i):
            print("Lo que usted ingresó no cumple con el formato correcto. Por favor reintentar.")
        else:
            return i


def input_range(elements: list[int],prompt="Ingrese su selección: "):
    while True:
        i = input(prompt).strip()
        if not i.isnumeric():
            print("Opción inválida. Debe ingresar un número\n")
        elif int(i) not in elements:
            print("Por favor ingrese un número válido.")
        else:
            return int(i)
        

def display_ayudantes_list(ayudantes_list: list[dict]):
    print("Ayudantes:")
    if not len(ayudantes_list):
        print("No hay ayudantes.")
        return
    for i, ayudante in enumerate(ayudantes_list):
        print(f"    {i+1}. {ayudante['nombre']} {ayudante['apellido']}")

def display_ayudante(ayudante: dict):
    print(f"    {ayudante['nombre']} {ayudante['apellido']}")
    print(f"    N° Alumno: {ayudante['n_alumno']}")
    print(f"    Estado:    {ayudante['estado']}")
    print(f"    Motivación:    {ayudante['motivacion']}")

def get_id_by_index(index, ayudantes):
    return ayudantes[index]["id"]


def menu_principal():
    print("BIENVENIDO AL SISTEMA DE ADMINISTRACIÓN DE AYUDANTES!")
    print("Por favor elija una opción:")
    print("1. Ver ayudantes")
    print("2. Crear ayudante")
    print("0. Salir")

    i = input_range([0, 1, 2])

    if i == 0:
        return Menus.salir,
    if i == 1:
        return Menus.lista_ayudantes,
    if i == 2:
        return Menus.crear_ayudante,



def ayudantes_menu():
    ayudantes = client.get_ayudantes_list()
    print("Elija una opción")
    display_ayudantes_list(ayudantes)
    print("    0. Volver")
    i = input_range([*range(len(ayudantes) + 1)])

    if i > 0:
        return Menus.detalles_ayudante, get_id_by_index(i-1, ayudantes)
    elif i == 0:
        return Menus.principal,

def detalles_ayudante(id_ayudante: int):
    ayudante = client.get_ayudante_by_id(id_ayudante)
    print("DETALLES AYUDANTE")

    display_ayudante(ayudante)

    print("    1. Ingresar motivación")
    print("    2. Asignar veredicto")
    print("    0. Volver")

    i = input_range([0, 1, 2])

    if i == 0:
        return Menus.lista_ayudantes,
    if i == 1:
        return Menus.ingresar_motivacion, id_ayudante
    if i == 2:
        return Menus.asignar_veredicto, id_ayudante

def crear_ayudante():
    print("CREAR AYUDANTE")
    nombre = regex_input(REGEX_NOMBRE, prompt="Ingrese el nombre: ")
    apellido = regex_input(REGEX_APELLIDO, prompt="Ingrese el apellido: ")
    n_alumno = regex_input(REGEX_N_ALUMNO, prompt="Ingrese el N° alumno: ")

    client.create_ayudante(nombre, apellido, n_alumno)

    return Menus.lista_ayudantes,

def ingresar_motivacion(id_ayudante: int):
    print("Ingrese la motivación: ")
    motivacion = input()

    client.fill_motivación(id_ayudante, motivacion)

    return Menus.detalles_ayudante, id_ayudante

def asignar_veredicto(id_ayudante: int):
    print("Desea aceptar o rechazar este ayudante? ")
    print("    1. Aceptar")
    print("    2. Rechazar")
    print("    0. Volver")
    i = input_range([0, 1, 2])

    if i == 1:
        client.asignar_veredicto(id_ayudante, "aceptado")
    elif i == 2:
        client.asignar_veredicto(id_ayudante, "rechazado")

    return Menus.detalles_ayudante, id_ayudante


def menu_loop():
    menu_actual = Menus.principal
    args = tuple()

    while True:
        if menu_actual == Menus.salir:
            print("Gracias por usar el sistema.")
            input("Presione la tecla Enter para cerrar.")
            exit(0)
        elif menu_actual == Menus.principal:
            menu_fn = menu_principal
        elif menu_actual == Menus.lista_ayudantes:
            menu_fn = ayudantes_menu
        elif menu_actual == Menus.detalles_ayudante:
            menu_fn = detalles_ayudante
        elif menu_actual == Menus.crear_ayudante:
            menu_fn = crear_ayudante
        elif menu_actual == Menus.ingresar_motivacion:
            menu_fn = ingresar_motivacion
        elif menu_actual == Menus.asignar_veredicto:
            menu_fn = asignar_veredicto
        
        menu_actual, *args = menu_fn(*args)

        print()


if __name__ == "__main__":
    menu_loop()
