from dotenv import dotenv_values
import math


def get_square(square):
    return square*(square*'*'+('\n'))


config = dotenv_values('.env')
string_square = config['square']
square = int(string_square)


squareSum = get_square(square)

print(squareSum)