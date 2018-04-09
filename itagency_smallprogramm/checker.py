# -*- coding: utf-8 -*-
import requests
"""
Программа, которая чекает какой ответ выдает сервер.
Это первая версия-заготовка, которую я хочу потом
использовать на каком-то живом проекте.

1. Сделать таймаут.
2. Сделать ввод данных из .csv и вывод в csv.
3. Первая колонка в файле url. Вторая — ответ сервера.
"""
count = 0
with open('url.txt', 'r') as file_url:
    with open('out.csv', 'w') as file_out:
        for line in file_url:
            count += 1
            line = line.rstrip()
            if len(line) > 7:
                url = requests.get(line.rstrip(), timeout=10)
                print('Обработано строк:', count, end='\r')
                print(line.rstrip() + ';' + str(url.status_code),
                      file=file_out)
