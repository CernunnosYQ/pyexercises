def multip2(numero1, numero2):
    ''' Funcion que multiplica dos números sin usar el simbolo de multiplicación

    '''
    res = 0
    for i in range(numero1):
        res += numero2

    return res


def nombre_invertido(nombre, apellido):
    ''' Funcion que recibe nombre y apellido y devuelve el nombre completo invertido

    '''
    nombre_completo = ' '.join((nombre, apellido))
    return nombre_completo[::-1]


def menor_lista(lista):
    ''' Funcion que devuelve el menor de una lista

    '''
    lista.sort()
    return lista[0]


def volumen_esfera(radio):
    ''' Funcion que calcula el volumen de una esfera a partir de su radio
        
        Formula de volumen de una esfera: 4/3 * PI * radio^2
    '''
    volumen = (4/3) * 3.1416 * pow(radio, 2)

    return volumen


def mayor_de_edad(edad):
    ''' Funcion que determina si un usuario es mayor de edad

    '''
    return edad >= 18


def es_par(numero):
    ''' Funcion que indica si un numero es par

    '''
    return numero%2 == 0


def contar_vocales(palabra):
    ''' Funcion que indica cuantas vocales tiene una palabra

    '''
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in  palabra.lower():
        for vocal in vocales:
            if letra == vocal:
                contador += 1
    return contador


def suma_lista(lista):
    ''' Funcion que suma una cantidad infinita de numeros

    '''
    suma = 0
    for numero in lista:
        suma += numero
    return suma


def agregar_contacto(nombre, telefono):
    ''' Funcion que agrega cintactos a un directorio

    '''
    contacto = ': '.join((nombre, telefono))

    with open('directorio.txt', 'a') as directorio:
        directorio.write(contacto + '\n')


def main():
#   Ejercicio 1:
    print('Funcion que multiplica dos números sin usar el simbolo de multiplicacion')
    numero1 = int(input('Introduce el primer número: '))
    numero2 = int(input('Introduce el segundo número: '))
    print(multip2(numero1, numero2))

#   Ejercicio 2:
    print('Funcion que recibe nombre y apellido y lo regresa al revés')
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    print(nombre_invertido(nombre, apellido))

#   Ejercicio 3:
    print('Funcion que devuelve el número menor de una lista')
    numeros = input('Escribe los números de la lista separados por espacios: ').split()
    print(menor_lista(numeros))

#   Ejercicio 4:
    print('Funcion que calcula el volumen de una esfera mediante su radio')
    radio = int(input('Introduce el radio de la esfera: '))
    print(volumen_esfera(radio))

#   Ejercicio 5:
    print('Funcion que indica si un usuario es o no mayor de edad')
    nombre = input('Introduce tu nombre: ')
    edad = input('Introduce tu edad: ')
    print('El usuario ' + nombre + (' es ' if mayor_de_edad(int(edad)) else ' no es ') + 'mayor de edad')

#   Ejercicio 6:
    print('Funcion que indica si un numero es par')
    numero = input('Introduce un número: ')
    print('El número es ' + ('par' if es_par(int(numero)) else 'impar'))

#   Ejercicio 7:
    print('Funcion que indica cuantas vocales tiene una palabra')
    palabra = input('Introduce una palabra: ')
    print('La palabra tiene ' + str(contar_vocales(palabra)) + ' vocales')

#   Ejercicio 8:
    print('Funcion que recibe una cantidad infinita de números hasta recibir un valor que no es un número')
    numeros = []
    while True:
        numero = input('Introduce un número: ')
        try:
            numero = int(numero)
            numeros.append(numero)
        except(ValueError):
            break
    print('El resultado de la suma es: ' + str(suma_lista(numeros)))

#   Ejercicio 9:
    print('Programa que agrega contactos a un archivo de texto')
    nombre = input('Introduce nombre: ')
    telefono = input('Introduce su telefono de contacto: ')
    agregar_contacto(nombre, telefono)
    print('El contacto ' + nombre + ' se ha añadido correctamente')


if __name__ == '__main__':
    main()
