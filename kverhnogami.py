# Программа воспроизводит текст наоборот
# Версия 1 и последняя!

word = input("Это я переверну: ")

rev = str()

while len(word) != len(rev):
    letter = len(rev) + 1
    rev += word[len(word) - letter]

print("\nПеревернул: {}".format(rev))
