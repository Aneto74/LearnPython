# -*- coding: utf-8 -*-
# Программа, которая отгадывает число, загаданное человеком
# Учусь использовать циклы
# Версия 1.3 — Теперь можно загадывать от 1 до 100 с проверкой
import random

max_number = 1000000000
min_number = 1

print('Тебе предоставляется возможность загадать число с',
      min_number, 'до', max_number)
print('А я его отгадаю!')

my_number = int(input('Загадай число:'))

while (my_number > max_number or my_number < min_number):
    print('Загадать число нужно с 1 до 100 включительно')
    my_number = int(input('Загадай число заново:'))

comp_number = ""
counts = 0

while comp_number != my_number:
    # 100 - 1 + 1 = 100 / 2 = 50
    # 49 - 1 + 1 = 49 / 2 = 24
    # 49 - 25 + 25 = 23 / 2 = 

    # 100 - 1 + 1 = 100 / 2 = 50
    # 100 - 50 + 1 = 51 / 2 = 26
    # 51 - 25
    comp_number = int(((max_number - min_number + 1) / 2) + min_number)
    # average_number_high = int((((max_number - min_number + 1) / 2) * 0.66) + min_number)
    # average_number_low = int((((max_number - min_number + 1) / 2) * 0.33) + min_number)
    # comp_number = random.choice([average_number_low, average_number_high])
    # comp_number = average_number
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
