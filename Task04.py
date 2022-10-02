# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

end = int(input('Введите диапазон элементов '))
start = end * (-1)

user_list = []

i = start
while i < end+1:
    user_list.append(i)
    i = i + 1
print(user_list)

a = int(input('Введите первый номер элемента списка '))
b = int(input('Введите второй номер элемента списка '))

result = user_list[a-1] * user_list[b-1]

print (result)