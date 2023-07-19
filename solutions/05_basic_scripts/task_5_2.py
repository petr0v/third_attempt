# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

request = input("Ввод IP-сети: ")
first_octet = int(request.split(".")[0])
second_octet = int(request.split(".")[1])
third_octet = int(request.split(".")[2])
fourth_octet = int(request.split(".")[-1].split("/")[0])
mask = request.split(".")[-1].split("/")[-1]
mask_bin = int(mask) * "1" + (32-int(mask)) * "0"
first_octet_mask = int(mask_bin[0:8],2)
second_octet_mask = int(mask_bin[8:16],2)
third_octet_mask = int(mask_bin[16:24],2)
fourth_octet_mask = int(mask_bin[24::],2)


template= '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''

print(template.format(first_octet, second_octet, third_octet, fourth_octet, mask, first_octet_mask, second_octet_mask, third_octet_mask, fourth_octet_mask))