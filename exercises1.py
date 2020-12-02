# -*- coding: utf-8 -*-

def ex1_max(num1, num2):
    """Función que retorna el mayor de dos números"""
    if num1 > num2:
        return num1
    else:
        return num2


def ex2_max3(num1, num2, num3):
    """Función que retorna el mayor de tres números"""
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


def ex3_len(string):
    """Función que retorna la longitud de una cadena"""
    counter = 0
    for _ in string:
        counter += 1
    return counter


def ex4_is_vowel(c):
    """Función que recibe un carácter, retorna True si el éste es una vocal
y False si no lo es.

Nota: Si se introduce una cadena de más de un carácter solo tomará en
cuenta el primer carácter de la cadena."""
    if len(c) > 1:
        c = c[0]

    c = c.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if c == vowel:
            return True
    return False


def ex5_sum(numbers):
    """Función que suma los números de una lista"""
    res = 0

    for n in numbers:
        res += int(n)

    return res


def ex5_multi(numbers):
    """Función que multiplica los números de una lista"""
    if len(numbers) == 0:
        res = 0
    else:
        res = 1

        for n in numbers:
            res *= int(n)

    return res


def ex6_reverse(string):
    """Función que recibe una cadena y la devuelve invertida"""
    #   reversed_string = string[::-1]   <-- So f*king easy xd
    reversed_string = ''

    for i in range(1, len(string) + 1):
        reversed_string += string[-i]

    return reversed_string


def ex7_is_palindrome(string):
    """Función que recibe una cadena y retorna True si esta es un palindromo.

Nota: Un palindromo es una palabra que escrita al revés se lee de la
misma forma. Ej: Radar invertido sigue siendo radaR"""
    string = string.lower()
    return string == string[::-1]


def ex8_superposition(list1, list2):
    """Función que compara 2 listas de números y retorna True si tienen
al menos un miembro en común y False si no."""
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


def ex9_char_generator(quantity, character):
    """Función que genera una cadena de texto repitiendo un carácter.
El carácter y la longitud de la cadena son definidos por el usuario.

Nota: Si se introduce una cadena de más de un carácter la función solo
tomará en cuenta el primer carácter de la cadena."""
    res = ''

    if len(character) > 1:
        character = character[0]

    for i in range(0, quantity):
        res += character

    return res


def ex10_generate_histogram(values, character):
    """Función que recibe una lista de valores y un carácter y devuelve un
histograma conformado por cadenas de caracteres (una cadena para cada valor)

Nota: Si se introduce una cadena de más de un carácter la función solo
tomará en cuenta el primer carácter de la cadena."""
    res = []

    if len(character) > 1:
        character = character[0]

    for value in values:
        res.append(ex9_char_generator(int(value), character))

    return res


def main():
    print('Ejercicio 1'.center(50, '='))
    print(ex1_max.__doc__)
    num1 = input('Introduce el primer número: ')
    num2 = input('Introduce el primer número: ')
    print('El número mayor es: ' + ex1_max(num1, num2) + '\n')

    print('Ejercicio 2'.center(50, '='))
    print(ex2_max3.__doc__)
    num1 = input('Introduce el primer número: ')
    num2 = input('Introduce el segundo número: ')
    num3 = input('Introduce el tercer número: ')
    print('El número mayor es: ' + ex2_max3(num1, num2, num3) + '\n')

    print('Ejercicio 3'.center(50, '='))
    print(ex3_len.__doc__)
    string = input('Introduce una palabra o frase: ')
    print('La longitud de la frase es de ' + str(ex3_len(string)) + ' caracteres \n')

    print('Ejercicio 4'.center(30, '='))
    print(ex4_is_vowel.__doc__)
    c = input('Introduce un carácter: ')
    print('El carácter ingresado ' + ('es' if ex4_is_vowel(c) else 'no es') + ' vocal \n')

    print('Ejercicio 5a'.center(30, '='))
    print(ex5_sum.__doc__)
    numbers = input('Introduce la lista de numeros separados por un espacio: ')
    print(str(ex5_sum(numbers.split())) + '\n')

    print('Ejercicio 5b'.center(30, '='))
    print(ex5_multi.__doc__)
    numbers = input('Introduce la lista de numeros separados por un espacio: ')
    print(str(ex5_multi(numbers.split())) + '\n')

    print('Ejercicio 6'.center(30, '='))
    print(ex6_reverse.__doc__)
    string = input('Introduce una palabra o frase: ')
    print('La frase invertida es: ' + ex6_reverse(string) + '\n')

    print('Ejercicio 7'.center(30, '='))
    print(ex7_is_palindrome.__doc__)
    string = input('Introduce una palabra o frase: ')
    print('La frase ingresada ' + ('es' if ex7_is_palindrome(string) else 'no es') + ' un palindromo \n')

    print('Ejercicio 8'.center(30, '='))
    print(ex8_superposition.__doc__)
    list1 = input('Introduce la primer lista separando los miembros con un espacio: ')
    list2 = input('Introduce la segunda lista separando los miembros con un espacio: ')
    print('Las listas ' + ('tienen' if ex8_superposition(list1.split(), list2.split()) else 'no tienen')
          + ' miembros en común \n')

    print('Ejercicio 9'.center(30, '='))
    print(ex9_char_generator.__doc__)
    quantity = int(input('Introduce la longitud deseada para la cadena: '))
    c = input('Introduce el caracter con el que deseas formar la cadena: ')
    print(ex9_char_generator(quantity, c) + '\n')

    print('Ejercicio 10'.center(30, '='))
    print(ex10_generate_histogram.__doc__)
    values = input('Introduce la lista de valores para el histograma separado por espacios: ')
    c = input('Introduce el caracter con el que deseas formar el histograma: ')
    histogram = ex10_generate_histogram(values.split(), c)
    for h in histogram:
        print(h)


if __name__ == '__main__':
    main()
