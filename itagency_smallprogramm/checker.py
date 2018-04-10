# -*- coding: utf-8 -*-
import requests
"""
Программа, которая чекает какой ответ выдает сервер.
В url.txt перечисляем URL, по которым потом соберем
ответ сервера.

Чтоб запустить на Windows и Mac → скачайте Python3 на 
https://www.python.org/ после запускайте *.py файлы как
exe'шник
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
