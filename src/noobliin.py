from dotenv import dotenv_values
from random import randint
import math


#функция(делаем фразу круче)
def nooblin(phrase,chance):

    random_value = randint(1,3) 


    #выбираем клёвое слово
    if random_value == 1:
        word = ' ну '
    if random_value == 2:
        word = ' блин '
    if random_value == 3:
        word = ' короче '   
         
    phrase = phrase.split(' ') # разделяем строку

    return word.join(phrase) # сшиваем строку с приколами
   
      

#Берем значения из .env
config = dotenv_values('.env')
string_chance = config['chance']
phrase = config['phrase']
chance = float(string_chance)


#Получаем итоговую переменную и выводим
out = nooblin(phrase,chance)
print(out)