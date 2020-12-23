import os


class GestorContactos:
    def __init__(self, nombre_archivo):
        self.nombre = nombre_archivo
        self.path = 'archivos/' + self.nombre + '.csv'
        self.contacto = {
            'ID': '',
            'Nombre': '',
            'Apellido': '',
            'Telefono': '',
            'Correo': ''}
        self.next_ID = 0

        if os.path.exists(self.path):
            with open(self.path, 'r') as archivo:
                archivo.seek(0, 0)
                aux = archivo.read().split('\n')[-2].split(',')[0]
                try:
                    self.next_ID = int(aux) + 1
                except ValueError:
                    self.next_ID = 0
        else:
            with open(self.path, 'w') as archivo:
                archivo.write((','.join(self.contacto.keys())) + '\n')
            self.next_ID = 0

    def crear_contacto(self, nombre, apellido, telefono, correo):
        self.contacto = {
            'ID': str(self.next_ID),
            'Nombre': nombre,
            'Apellido': apellido,
            'Telefono': telefono,
            'Correo': correo}

        with open(self.path, 'a') as archivo:
            archivo.write((','.join(self.contacto.values())) + '\n')
            self.next_ID += 1

    def mostrar_contactos(self):
        with open(self.path, 'r') as archivo:
            linea = archivo.readline()
            while linea:
                celdas = linea.split(',')
                if len(celdas) > 1:
                    self.imprimir_contacto(celdas)
                    linea = archivo.readline()

    def buscar_contacto(self, clave, valor):
        with open(self.path, 'r') as archivo:
            linea = archivo.readline()
            while linea:
                celdas = linea.split(',')
                self.contacto = {
                    'ID': celdas[0],
                    'Nombre': celdas[1],
                    'Apellido': celdas[2],
                    'Telefono': celdas[3],
                    'Correo': celdas[4][:-1]}

                if self.contacto[clave] == valor:
                    self.imprimir_contacto(celdas)
                    break

                linea = archivo.readline()

    def eliminar_contacto(self, ID):
        temp_path = self.path + '.tmp'
        cambiado = False
        with open(self.path, 'r') as archivo:
            linea = archivo.readline()

            while linea:
                celdas = linea.split(',')
                self.contacto = {
                    'ID': celdas[0],
                    'Nombre': celdas[1],
                    'Apellido': celdas[2],
                    'Telefono': celdas[3],
                    'Correo': celdas[4][:-1]}

                if self.contacto['ID'] == ID:
                    self.imprimir_contacto(celdas)
                    seguro = input(
                        '¿Seguro que deseas eliminar el contacto? [s]í / [N]o')
                    if seguro.lower() == 's':
                        cambiado = True
                        linea = archivo.readline()
                        continue
                    else:
                        os.remove(temp_path)
                        break
                else:
                    with open(temp_path, 'a+') as temp:
                        temp.write((','.join(self.contacto.values())) + '\n')

                linea = archivo.readline()

        if cambiado:
            os.remove(self.path)
            os.rename(temp_path, self.path)
        else:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def imprimir_contacto(self, lista):
        lista_imprimible = '|'
        lista_imprimible += (lista[0].center(6) + '|')
        lista_imprimible += (lista[1].center(20) + '|')
        lista_imprimible += (lista[2].center(20) + '|')
        lista_imprimible += (lista[3].center(20) + '|')
        lista_imprimible += (lista[4][:-1].center(34) + '|')

        print(lista_imprimible)


def main(nombre_archivo):
    print('Bienvenido al administrador de contactos')

    operaciones_realizadas = False
    gestor = GestorContactos(nombre_archivo)

    while not operaciones_realizadas:
        print('¿Qué operacion deseas realizar?')
        print(
            '[C]rear contacto\n[V]er todos los contactos\n[B]uscar contacto\n[E]liminar contacto')

        operacion = input('Operación: ').lower()

        if operacion == 'c':
            nombre = input('Introduce el nombre: ')
            apellido = input('Introduce el apellido: ')
            telefono = input('Introduce el número de teléfono: ')
            correo = input('Introduce el correo: ')

            gestor.crear_contacto(nombre, apellido, telefono, correo)

        elif operacion == 'v':
            gestor.mostrar_contactos()

        elif operacion == 'b':
            clave = input('Introduce el campo por el que deseas buscar: ')
            valor = input('Introduce el valor a buscar: ')
            gestor.buscar_contacto(clave, valor)

        elif operacion == 'e':
            ID = input('Introduce el ID del contacto a eliminar: ')

            gestor.eliminar_contacto(ID)

        else:
            print('Operacion invalida')
            continue

        operaciones_realizadas = input(
            '¿Deseas realizar otra operacion? [s]í / [N]o: ').lower() != 's'


if __name__ == '__main__':
    main('Contactos')
