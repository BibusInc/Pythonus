from dotenv import dotenv_values
import math


#функция
def get_square(square):
    return square*(square*'*'+('\n'))


#Берем значения из .env
config = dotenv_values('.env')
string_square = config['square']
square = int(string_square)


#Получаем итоговую переменную и выводим
squareSum = get_square(square)

print(squareSum)