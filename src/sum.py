from dotenv import dotenv_values
import math


#функция
def get_sum(sum):
		for i in range(0,501):
			sum += i
			i += 1
		return sum


#Берем значения из .env
config = dotenv_values('.env')
string_sum = config['sum']
sum = int(string_sum)


#Получаем итоговую переменную и выводим
FinalSum = get_sum(sum)
print(FinalSum)