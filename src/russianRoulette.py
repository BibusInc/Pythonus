from random import randint
from dotenv import dotenv_values

user_input = None

def gun(user_input):
	while True:

		user_input = input()
		random_value = randint(1,6)

		if (random_value>5):
			raise Exception(DeathPhrase)
		else:
			print('ладно')

		if (user_input == 'вырубай'):
			break



config = dotenv_values('.env')
DeathPhrase = config['DeathPhrase']


#Получаем итоговую переменную и выводим
print(gun(user_input))
