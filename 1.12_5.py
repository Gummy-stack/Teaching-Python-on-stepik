"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три
строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
"""
a = int(input())
b = int(input())
c = int(input())
if (b <= a >= c) and (b >= c):
    print(a, '\n',c, '\n', b)
elif (b <= a >= c) and (b <= c):
    print(a, '\n', b, '\n', c)
elif (a <= b >= c) and (a >= c):
    print(b, '\n', c, '\n', a)
elif (a <= b >= c) and (a <= c):
    print(b, '\n', a, '\n', c)
elif (a <= c >= b) and (a >= b):
    print(c, '\n', b, '\n', a)
elif (a <= c >= b) and (a <= b):
    print(c, '\n', a, '\n', b)
