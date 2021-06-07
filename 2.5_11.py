"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
"""
s = [int(i) for i in input().split()]
s.sort()
buff = []
for i in s:
    if s == 1:
        s.pop(0)
    elif s.count(i) > 1 and i not in buff:
        buff.append(i)
print(*buff, end=' ')

"""a, b = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and b.count(i) == 0:
        b.append(i)
for i in b:
    print(i, end=" ")"""
