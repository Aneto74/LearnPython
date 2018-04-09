import random
# Выводим список рандомом

listing = ["Первый", "Второй", "Третий"]

random_choice = random.choice(listing)
print()

while len(listing) != 0:
    print(random_choice)
    listing.remove(random_choice)
    if len(listing) > 0:
        random_choice = random.choice(listing)
    else:
        print("\nРасчёт вразнобой закончен!\n")
