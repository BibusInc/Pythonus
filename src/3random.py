import random

arr = []

for i in range(1, 10):
 	arr.append('да')
 	arr.append('я')
 	arr.append('массив')


random.shuffle(arr)			#перемешиваем
list.sort(arr)				#сортируем по алфавиту
list.sort(arr, key = len)	#сортируем по длине

print(arr) 		 		

