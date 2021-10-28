from dotenv import dotenv_values
import math


#функция
def get_square(square):
    return square*(square*'*'+('\n'))


#Берем значения из .env
config = dotenv_values('.env')
string_square = config['square']


#Исключения 
try:
    square = int(string_square)

except ValueError:
    raise ValueError(f'Не могу превратить значение {string_square} в число')

if square <= 0:
    raise ValueError('Сторона квадрата должна быть больше нуля')


#Получаем итоговую переменную и выводим
squareSum = get_square(square)

print(squareSum)