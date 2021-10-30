from dotenv import dotenv_values


user_input = None

def bull(user_input):

	while True:
		user_input = input()	
		print(f'Все говорят {user_input}, а ты купи бычка')

		if user_input == ('заверните два'):
			break


#Получаем итоговую переменную и выводим
print(bull(user_input))





