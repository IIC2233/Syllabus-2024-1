from math import ceil


class SitioWeb:

    def __init__(self, url, mail, ip):
        self.url = url
        self.mail = mail
        self.ip = ip
        self.reclamos = []

    def recibir_reclamo(self, mail_usuario, texto):
        self.reclamos.append([mail_usuario, texto])


class DCChrome:
    def __init__(self, mail):
        self.mail = mail
        self.sitios = []
        self.back_stack = []
        self.forward_stack = []

    def cargar_paginas(self, nombre_archivo):
        with open(nombre_archivo) as archivo:
            primera = archivo.readline().strip().split(",")
            # Iteramos sobre el archivo, lo que nos va entregando las lineas
            for linea in archivo:
                datos_sitio = linea.strip().split(",")
                dic_sitio_web = {primera[i]: datos_sitio[i] for i in range(3)}
                self.sitios.append(SitioWeb(**dic_sitio_web))

    def listado_de_sitios(self, sitio_anterior=-1):
        index = 0
        while True:
            sitio_2 = ""
            sitio_3 = ""
            if index + 1 < len(self.sitios):
                sitio_2 = self.sitios[index + 1].url
            if index + 2 < len(self.sitios):
                sitio_3 = self.sitios[index + 2].url
            print("Listado de sitios")
            print("-" * 62)
            print(f"{self.sitios[index].url:^20.20s}|{sitio_2:^20.20s}|{sitio_3:^20.20s}")
            print(f"{1: ^20d}|{2: ^20d}|{3: ^20d}")
            print("-" * 62)
            print("1. Sitio 1")
            print("2. Sitio 2")
            print("3. Sitio 3")
            print("4. ->")
            print("5. <-")
            print("6. Salir")
            if sitio_anterior != -1:
                # Si es que ya veníamos de un sitio damos la opción de volver
                print("7. Volver al sitio")
            nro = input("Elija una opción: ")
            print()
            if ((not sitio_2) and (nro == "2")) or ((not sitio_3) and (nro == "3")):
                # Si es que no hay segundo o tercer sitio y el input es 2 o 3
                # pasamos a la siguiente iteración
                continue
            if nro == "1" or nro == "2" or nro == "3":
                self.forward_stack = []
                self.entrar_a_sitio(index + int(nro) - 1)
                break
            if nro == "4":
                if index + 3 < len(self.sitios):
                    index += 3
            if nro == "5":
                if index - 3 >= 0:
                    index -= 3
            elif nro == "6":
                break
            elif nro == "7" and sitio_anterior != -1:
                # Si es que volvemos al sitio anterior debemos sacar el sitio
                # del back_stack (deshacemos lo que se hace en la linea 127)
                self.back_stack.pop()
                self.entrar_a_sitio(sitio_anterior)
                break

    def entrar_a_sitio(self, nro_sitio):
        while True:
            print(f"{self.sitios[nro_sitio].url:^62s}")
            print(f"{self.sitios[nro_sitio].ip:^62s}")
            print(f"{self.sitios[nro_sitio].mail:^62s}")
            print("-" * 62)
            print("Reclamos:")
            print()
            for mail_user, reclamo in self.sitios[nro_sitio].reclamos:
                print(f"from: {mail_user}")
                print(f"to: {self.sitios[nro_sitio].mail}")
                for i in range(ceil(len(reclamo) / 62)):
                    print(f"{reclamo[62 * i: 62 * (i + 1)]:62s}")
                print()
            print("-" * 62)
            sitio_atras = ""
            sitio_adelante = ""
            if self.back_stack:
                sitio_atras = self.sitios[self.back_stack[-1]].url
            if self.forward_stack:
                sitio_adelante = self.sitios[self.forward_stack[-1]].url
            print(f"1. Atrás: {sitio_atras}")
            print(f"2. Adelante: {sitio_adelante}")
            print("3. Escribir reclamo")
            print("4. Listado de sitios")
            print("5. Salir")
            nro = input("Elija una opción: ")
            print()
            if nro == "1":
                if self.back_stack:
                    nuevo_sitio = self.back_stack.pop()
                    self.forward_stack.append(nro_sitio)
                    self.entrar_a_sitio(nuevo_sitio)
                    break
            if nro == "2":
                if self.forward_stack:
                    nuevo_sitio = self.forward_stack.pop()
                    self.back_stack.append(nro_sitio)
                    self.entrar_a_sitio(nuevo_sitio)
                    break
            if nro == "3":
                reclamo = input("Escriba su reclamo: ")
                self.sitios[nro_sitio].reclamos.append([self.mail, reclamo])
            if nro == "4":
                # Si es que entramos al listado de sitios ponemos
                # temporalmente al sitio en el back_stack, por si
                # luego entramos a otro sitio
                self.back_stack.append(nro_sitio)
                self.listado_de_sitios(nro_sitio)
                break
            if nro == "5":
                break


navegador = DCChrome("tu.mail@uc.cl")
navegador.cargar_paginas("data.csv")
navegador.listado_de_sitios()
