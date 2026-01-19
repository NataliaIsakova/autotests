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
git push origin master