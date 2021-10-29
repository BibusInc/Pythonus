from dotenv import dotenv_values
from random import randint
import math


#Получаем случайные клёвые слова
def coolword(words):
    words = ['ну','короче','блин']
    random_value1 = randint(0,2)
    return(words[random_value1]) 


#Делаем фразу круче
def nooblin(phrase,chance):

    phrase = phrase.split(' ')  
    length = len(phrase)       

    for i in range (int(chance*10)):
        word = coolword(words)      
        random_value2 = randint(1,length) 
        phrase.insert(random_value2, word)
        i+=1

    return ' '.join(phrase)
   

#Берем значения из .env
config = dotenv_values('.env')
string_chance = config['chance']
phrase = config['phrase']
words = config['words']
chance = float(string_chance)


#Получаем итоговую переменную и выводим
out = nooblin(phrase,chance)
print(out)