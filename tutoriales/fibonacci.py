#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que contiene funciones para crear la serie de Fibonacci
Permite ejecutar el módulo como script

@author: Roberto Muñoz
"""


def fib1(n):
    """ Imprime en pantalla la serie Fibonacci hasta n """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """ Retorna una lista que contiene la serie Fibonacci hasta n """
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

if __name__ == "__main__":
    import sys
    fib1(int(sys.argv[1]))