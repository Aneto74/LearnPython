# -*- coding: utf-8 -*-
# Программа «Анаграмма». Компьютер зашифровывает слова,
# а тебе нужно его отгадать.
# v1.0 Реализовал цикл, если ответ не верен + начисление очков.

import random

words = ("стол", "стул", "кошка", "схема")
word = random.choice(words)

correct = word
anagram = str()

while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[position + 1:]

letters = len(anagram)

points = 0
rightchoice = 20
badchoice = -5

print("\nАнаграмма загаданного слова: {}".format(anagram))
guess = input("Введите загаданое слово: ")

while correct != guess:
    print("\nНеверно! ", end="")
    points += badchoice
    randletter = random.randrange(len(correct))
    letter = correct[randletter]
    print("У этого слова {} буква «{}».".format(randletter, letter))
    guess = input("\nПопробуйте снова: ")

points += rightchoice
print("\nПоздравляю, вы отгадали, это действительно было слово «{}»".format(correct))
print("\nВы заработали {} очков".format(points))
