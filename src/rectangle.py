from dotenv import dotenv_values
import math


#функция
def get_square(width,length):
    return width*length


#Берем значения из .env
config = dotenv_values('.env')
string_length = config['length']
string_width = config['width']
length = int(string_length)
width = int(string_width)


#Получаем итоговую переменную и выводим
square = get_square(width,length)
print(f'Площадь прямоугольника длиной {length} и шириной {width} равна {square}')