Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого
введенного нуля выводит сумму полученных на вход чисел.
"""
# Буфер - пустой список
result = []
while True:
    a = int(input())
    if a == 0:
        print()
        break
    else:
        result.append(a)
# печатаем результат функции sum() - выдает сумму чисел в интерируемом объекте (например список, кортеж)
print(sum(result))

"""
a = int(input())
s = a
while a != 0:
    a = int(input())
    s += a
print(s)
"""
