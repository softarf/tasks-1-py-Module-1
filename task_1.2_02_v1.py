
# coding: utf-8        # -*- coding: utf-8 -*-
'''
https://replit.com/@softar/ZigzagAcceptableCallbacks#main.py

Не знал как правильно надо было организовать решение: Сначала вводятся все данные призывника,
а потом делается анализ на годен/не годен, и в какие войска. Или, по мере ввода,
сразу анализируется каждое введённое значени. Поэтому сделал оба варианта.
'''
#           Вариант 1

print('\n    Задача 2_v1. Раздел 1.2\n')
height = int(input(' Введите рост призывника: '))
old = int(input(' Введите возраст призывника: '))
children = int(input(' Укажите количество детей: '))
student = input(' Учится ли он сейчас (y/n): ')
if height >= 160 and 18 <= old <= 27 and children < 2 and student == 'n':
    if 160 <= height <= 169:
        print('\n Годен. Танковые войска.\n')
    elif 170 <= height <= 179:
        print('\n Годен. Морской флот.\n')
    elif 180 <= height <= 200:
        print('\n Годен. Десантные войска.\n')
    elif height > 200:
        print('\n Годен. Другие войска.\n')
else:
    print('\n К службе не годен.\n')

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды