# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from math import factorial

def multiplication (n):

    result = []

    while n > 0:
        
        result.append(factorial(n))
        n -= 1
        
    result.reverse()
    print ('Набор произведений от 1 до вашего числа:', result)

n = int(input('Введите число: '))
multiplication(n)