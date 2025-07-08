'''1'''
F = 200
C = (F -32)*5/9
print(C)

'''2'''
'''операторы'''
'''зачадача №1'''
gramm = 12345
print('В 12345 Граммах содержиться' + ' ' + str(gramm//1000) +  ' ' + 'полных килограмм')

'''зачадача №2'''

numb = 4353553
last_digit = int(str(numb)[-1])
print('последняя цифра числа 4353553:' + str(last_digit))

'''зачадача №3'''

number = -2
result =  number % 2 == 0 and number > 0
if result:
    print('число' + ' ' + str(number) + ' ' + 'является положительным и четным')
else:
    print('число' + ' ' + str(number) +' ' + 'не походит под условие')

'''зачадача №4'''

num = 150

if num > 0 and num < 100:
    print('Число' + ' ' + str(num) + ' ' + 'находится в переделах диапазона 0 - 100')
else:
    print('Число выходит' + ' ' + str(num) + ' ' + 'за пределы диапазона 0 - 100')


'''зачадача №5'''

numbr =  8

if numbr % 3 == 0:
    print('Число' + str(numbr) + ' '  'кратно 3')
else:
    print('Число' + ' ' +  str(numbr) + ' '  ' не кратно 3')


''' Коллекции данных'''
'''зачадача №1'''
fruits = ["яблоко", "банан", "вишня"]
fruits.append(('ежевика'))
print(fruits)

'''зачадача №2'''
fruits.remove('банан')
print(fruits)

'''зачадача №3'''
print(fruits[1])

'''зачадача №4'''

print(fruits[0:2])

'''зачадача №5'''
colors = ['red', 'green', 'blue']
colors[1] = 'yellow'

print(colors)

'''зачадача №6'''

print(len(colors))

'''зачадача №7'''
student = {'name': 'Alex', 'age' : '20'}
student['grade'] = 'A'
print(student)

'''зачадача №8'''

student['grade'] = 'B'
print(student)

'''зачадача №9'''
del student['age']
print(student)

'''зачадача №10'''

print(student['name'])

'''зачадача №11'''

if ('grade' in student):
    print('грейд' + ' ' + student['grade'] + ' '  + 'найден')
else:
    print('грейд' + ' ' + student['grade'] + ' ' + 'не найден')

    '''зачадача №12'''

student['address'] = {'city': 'Moscow', 'street': 'Lenina'}
print(student)

'''зачадача №13'''
student['marks'] = [10, 30, 80]
student['marks'][-1] = 70
print(student)


'''зачадача №14'''

studens = [{'name': 'Alex', 'age': 20}, {'name': 'Olga', 'age': 21}]
studens[0]['age'] = 22
studens[1]['age'] = 18
print('studens', studens)

'''зачадача №15'''

colors = ['red', 'green', 'blue']

print('red' in colors, len(colors))
