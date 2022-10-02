# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

import numbers
from unicodedata import decimal


def number_summ (number):

    result = []
    while (number % 1) > 0:
        number = round(number * 10, 7)

    while number > 0:
        result.append(number % 10)
        number = number // 10
    print ('Сумма цифр вашего числа:', int(sum(result)))
    
number = float(input('Введите любое число: '))

number_summ (number)