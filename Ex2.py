"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = [b'class', b'function', b'method']

for w in words:
    print('тип переменной: {}\n'.format(type(w)))
    print('содержание переменной - {}\n'.format(w))
    print('длинна строки: {}\n'.format(len(w)))
