"""
Программа «Считалочка» v2.0
Считает от и до числа, который задал пользователь.
Пользователь так же задает интервал с которым вы выведем числа.
Проверяем правильность ввода.
"""

direction = input("Будем считать вперед или назад? ")
direction = direction.lower()

while direction != "вперед" and direction != "назад":
    print('\nВам нужно написать «вперед» или «назад»')
    direction = input('В каком направлении будем считать? ')
    direction = direction.lower()

if direction == "вперед":
    interval = 1
elif direction == "назад":
    interval = -1

start = int(input("\nВведите значение от которого надо считать: "))
end = int(input("Теперь введите значение до которого надо считать: "))

while direction == "вперед":
    if end <= start:
        print("\nПервое число должно быть меньше второго")
        print("К примеру, «от -1 до 5» или «от 5 до 180»")
        print("Оба числа не должны равняться друг-другу")
        print("\nВозможно вы хотели написать от {} до {}".format(end, start))
        start = int(input("\nВведите значение ОТ которого надо считать: "))
        end = int(input("Теперь введите значение ДО которого надо считать: "))
    elif end > start:
        break

while direction == "назад":
    if end >= start:
        print("\nПервое число должно быть больше второго")
        print("К примеру, «от 5 до -1» или «от 180 до 5»")
        print("Оба числа не должны равняться друг-другу")
        print("\nВозможно вы хотели написать от {} до {}".format(end, start))
        start = int(input("\nВведите значение ОТ которого надо считать: "))
        end = int(input("Теперь введите значение ДО которого надо считать: "))
    elif end < start:
        break

if end > start:
    end += 1
else:
    end = end - 1

print('\nТеперь нам нужно решить с каким интервалом мы будем выводить число.')
print('Допустим это будет «1 3 5 7» через 2 или «1 5 9» — через 4')
t = int(input('\nС каким интервалом выводить?'))

interval = interval * t

for i in range(start, end, interval):
    print(i, end=" ")
