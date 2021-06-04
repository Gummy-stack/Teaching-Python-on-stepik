"""
Вывести чётные
Необходимо вывести все четные числа на отрезке [a; a * 10].
"""
a = int(input())
otr = ()
for i in range(a, a * 10 + 1):
    if i % 2 == 0:
        otr += (i,)
print(otr)
"""
otr = int(input())
print(tuple(range(otr + otr % 2, otr * 10 + 1, 2)))
"""
