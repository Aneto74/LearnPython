import random

"""
Программа «Поле Чудес». Загадано слово.
Нужно отгадать его с одной попытки.
Дается 6 попыток для букв.
"""

WORDS = ("солнцеликий", "воскрешение", "некромантия", "канибализм")
misstakes = 0
question = random.choice(WORDS)
letter = []

# Пользователю даем спросить 6 раз букву.
# После 6 попыток — спрашиваем итоговое слово.
# Если не верно — проиграл.

letters = len(question)
print("Добро пожаловать в игру «Поле чудес»!", end=" ")
print("Вам нужно отгадать слово из {} букв. У вас 6 возможностей открыть буквы!".format(letters))
boxes = "_" * letters

while misstakes < 7 and boxes != question:
    print("{}".format(boxes))
    guess_letter = input("Какую буквы хотите открыть? ")
    guess_letter = guess_letter.lower()
    print("\nНа данный момент использованы эти буквы: {}".format(letter))
    while guess_letter in letter:
        print("Вы уже называли эту букву «{}»".format(guess_letter))
        print("У вас еще есть {} попытки!\n".format(7 - misstakes))
        guess_letter = input("Еще один шанс, какую букву хотите открыть? ")
        guess_letter = guess_letter.lower()
    letter.append(guess_letter)
    if guess_letter in question:
        print("\nДа, буква «{}» есть в этом слове!".format(guess_letter))
        new = ""
        for i in range(len(question)):
            if guess_letter == question[i]:
                new += guess_letter
            else:
                new += boxes[i]
        boxes = new
    else:
        print("\nНет, буквы «{}» в этом слове!".format(guess_letter))
        print("У вас еще есть {} попытки!\n".format(7 - misstakes))
        misstakes += 1

if misstakes == 7:
    print("\nПопытки по отгадыванию букв закончились!")
    print("Сейчас слово выглядит так: {}".format(boxes))
    boxes = input("\nКакое слово содержится в этих буквах? ")
    boxes = boxes.lower()
    if boxes == question:
        print('Да! Мы загадали {}! Поздравляю, вы выиграли!'.format(question))
        exit(0)
    else:
        print('Увы! Вы проиграли!')
        exit(0)
else:
    print('Да! Мы загадали {}! Поздравляю, вы выиграли!'.format(question))
