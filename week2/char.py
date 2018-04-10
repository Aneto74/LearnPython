"""
Программа «Характеристики».
Распределяем + к характеристикам

Предоставляем выбор через if и while
"""

dex = 0
stg = 0
wis = 0
tgn = 0

char_point = 30
choice = -1

while char_point > 0 and choice != 0:
    print("""
Распределите характеристики:
1 - Сила — {} (убрать — 9)
2 - Ловкость — {} (убрать - 8)
3 - Мудрость — {} (убрать - 7)
4 - Выносливость — {} (убрать - 6)
0 - Выйти

Для распределения доступно: {}
""".format(stg, dex, wis, tgn, char_point))

    choice = int(input("Твой выбор: "))
    if choice == 0:
        print("Пока!")
    elif choice == 1:
    	print("В «Силу» добавлен 1 балл.")
    	stg += 1
    	char_point -= 1
    	print("Теперь в «Силе» — {}".format(stg))
    elif choice == 2:
        print("В «Ловкость» добавлен 1 балл.")
        dex += 1
        char_point -= 1
        print("Теперь в «Ловкость» — {}".format(dex))
    elif choice == 3:
        print("В «Мудрость» добавлен 1 балл.")
        wis += 1
        char_point -= 1
        print("Теперь в «Мудрости» — {}".format(wis))
    elif choice == 4:
        print("В «Выносливость» добавлен 1 балл.")
        tgh += 1
        char_point -= 1
        print("Теперь в «Выносливости» — {}".format(tgh))
    elif choice == 9:
        print("В «Силу» добавлен 1 балл.")
        stg -= 1
        char_point += 1
        print("Теперь в «Силе» — {}".format(stg))
    elif choice == 8:
        print("В «Ловкость» добавлен 1 балл.")
        dex -= 1
        char_point += 1
        print("Теперь в «Ловкость» — {}".format(dex))
    elif choice == 7:
        print("В «Мудрость» добавлен 1 балл.")
        wis -= 1
        char_point += 1
        print("Теперь в «Мудрости» — {}".format(wis))
    elif choice == 6:
        print("В «Выносливость» добавлен 1 балл.")
        tgh -= 1
        char_point += 1
        print("Теперь в «Выносливости» — {}".format(tgh))

if char_point == 0:
    print("""
		Все характеристики распределены!

		Сила — {}
		Ловкость — {}
		Мудрость — {}
		Выносливость — {}

		""".format(stg, dex, wis, tgn))
