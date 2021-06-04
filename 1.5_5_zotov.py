"""
Большое число
С клавиатуры вводится одно число, и вам необходимо определить, действительно ли оно большое.
Скажем, если число по модулю больше миллиарда, то напечатаем "Да, это большое число", иначе выведем
"Нет, это не такое уж и большое число". ﻿
Примечание: возможно, функция abs() упростит вам задачу. Выяснение того, как она применяется, предоставим вам самим.
"""
a = int(input())
if abs(a) > 1000000000:
    print('Да, это большое число')
else:
    print('Нет, это не такое уж и большое число')