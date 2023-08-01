# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

work = dict(access = access_template, trunk = trunk_template)
mode_work = input("Введите режим работы интерфейса (access/trunk): ")
choose_your_destiny = dict(access= "Введите номер VLAN:", trunk= 'Введите разрешенные VLANы:')
interface = input("Введите тип и номер интерфейса: ")
vlan = input(choose_your_destiny[mode_work])

print('interface {}'.format(interface))
print('\n'.join(work[mode_work]).format(vlan))