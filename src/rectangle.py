from dotenv import dotenv_values
import math


def get_square(width,length):
    return width*length


config = dotenv_values('.env')
string_length = config['length']
string_width = config['width']
length = int(string_length)
width = int(string_width)


square = get_square(width,length)
print(f'Площадь прямоугольника длиной {length} и шириной {width} равна {square}')