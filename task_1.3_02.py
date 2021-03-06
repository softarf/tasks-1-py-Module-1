
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 2. Раздел 1.3')
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мёд', 50, 'мл.'],
      ]
  ]
]
person = int(input('\n Укажите количество ожидаемых гостей: '))
print('\n     Необходимо закупить:')

#        Первый вариант
'''
n = 1
for dish in cook_book:
    print(f'\n     {dish[0].capitalize()}:')
    for component in dish[1]:
        print(f'{n:>3}. {component[0]}, {component[1] * person} {component[2]}')
        n += 1
'''

#        Второй вариант
n = 1
for dish_name, composition in cook_book:
    print(f'\n     {dish_name.capitalize()}:')
    for ingradient, weight, unit in composition:
        print(f'{n:>3}. {ingradient}, {weight * person} {unit}')
        n += 1

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
