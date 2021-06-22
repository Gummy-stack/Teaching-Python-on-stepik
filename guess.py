# Эта игра по угадыванию чисел.
import random

guessTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадываю число от 1 до 20.')

for guessTaken in range(6):
    print('Попробуй угадать.') # Четыре пробела перед именем функции print
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.') # Восемь пробелов перед именем функции print

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('Отлично, ' + myName + '! Ты справился с ' + guessTaken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')
