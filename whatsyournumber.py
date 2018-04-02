# -*- coding: utf-8 -*-
# Программа, которая отгадывает число, загаданное человеком
# Учусь использовать циклы
# Версия 1.2 — Теперь можно загадывать от 100 млрд до -100 млрд
import random

print('Тебе предоставляется возможность загадать число')
print('А я его отгадаю!')

my_number = int(input('Загадай число:'))

comp_number = ""
max_number = 99999999999999
min_number = -99999999999999
counts = 0

while comp_number != my_number:
    comp_number = random.randint(min_number, max_number)
    print('Компьютер: «Может это число', comp_number, '?»')
    counts += 1
    if comp_number < my_number:
        min_number = comp_number + 1
        print('Ты: Это число больше, чем', comp_number)
    elif comp_number > my_number:
        max_number = comp_number - 1
        print('Ты: Это число меньше, чем', comp_number)
    else:
        print('Ты: да, это было', comp_number, ':(')

if counts == 1:
    text_counts = "попытку!"
elif 1 < counts < 5:
    text_counts = "попытки"
elif counts > 4:
    text_counts = "попыток"

print("Компьютер: Ха-ха-ха, я отгадал твое число! За", counts, text_counts)
