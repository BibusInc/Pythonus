from dotenv import dotenv_values
import math


#функция
def get_square(width,length):
    return width*length


#Берем значения из .env
config = dotenv_values('.env')
string_length = config['length']
string_width = config['width']


#Исключения 
try:
    length = int(string_length)

except ValueError:
    raise ValueError(f'Не могу превратить значение {string_length} в число')

if length <= 0:
    raise ValueError('Длина стороны должна быть больше нуля')

try:
    width = int(string_width)

except ValueError:
    raise ValueError(f'Не могу превратить значение {string_width} в число')

if width <= 0:
    raise ValueError('Ширина стороны должна быть больше нуля')    


#Получаем итоговую переменную и выводим
square = get_square(width,length)
print(f'Площадь прямоугольника длиной {length} и шириной {width} равна {square}')