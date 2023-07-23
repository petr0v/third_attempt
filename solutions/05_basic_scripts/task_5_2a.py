# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    ``, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
request = input("Ввод IP-сети: ")
first_octet = int(request.split(".")[0])
second_octet = int(request.split(".")[1])
third_octet = int(request.split(".")[2])
fourth_octet = int(request.split(".")[-1].split("/")[0])
mask = request.split(".")[-1].split("/")[-1]
mask_zero = (32-int(mask)) * "0"
mask_bin = int(mask) * "1" + (32-int(mask)) * "0"
first_octet_mask = int(mask_bin[0:8],2)
second_octet_mask = int(mask_bin[8:16],2)
third_octet_mask = int(mask_bin[16:24],2)
fourth_octet_mask = int(mask_bin[24:],2)
new_mask = int(mask)
bin_host = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(first_octet, second_octet, third_octet, fourth_octet)
bin_changed = bin_host[new_mask:].replace(bin_host[new_mask:],mask_zero)
bin_network = bin_host[:new_mask] + bin_changed
bin_network_octet1 = int(bin_network[0:8],2)
bin_network_octet2 = int(bin_network[8:16],2)
bin_network_octet3 = int(bin_network[16:24],2)
bin_network_octet4 = int(bin_network[24:],2)

template= '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''

print(template.format(bin_network_octet1, bin_network_octet2, bin_network_octet3, bin_network_octet4, mask, first_octet_mask, second_octet_mask, third_octet_mask, fourth_octet_mask))