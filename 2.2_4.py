"""
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.
"""
while True:
    res = int(input())
    if res < 10:
        continue
    elif res > 100:
        break
    else:
        print(res)
