from dotenv import dotenv_values
import math


def get_sum(sum):
		for i in range(0,501):
			sum += i
			i += 1
		return sum


config = dotenv_values('.env')
string_sum = config['sum']
sum = int(string_sum)


FinalSum = get_sum(sum)
print(FinalSum)