import string

a = input('Вход (от 0 до 99): ') # по умолчанию вводится строка
a = a.strip()

if not(1 <= len(a) <= 2):
    print('Вы должны ввести число')
    exit(1)
    
b = '0123456789' #проверка строки на наличие этих чисел в строке
    
if a[0] not in b
    print('Вы должны ввести число')
    exit(1)
    
if len(a) > 1 and a[1] not in b # если в строке 1 символ, то без проверка длины будет ошибка
    print('Вы должны ввести число')
    exit(1)
    
a = int(a)
    
if not(0 <= a <= 99)
    print('Вы должны ввести число')
    exit(1)
    
answer = ''

if a // 10 = 2:
    answer += 'двадцать '
if a // 10 = 3:
    answer += 'тридцать '
if a // 10 = 4:
    answer += 'сорок '
if a // 10 = 5:
    answer += 'пятьдесят '
if a // 10 = 6:
    answer += 'шестьдесят '
if a // 10 = 7:
    answer += 'семьдесят '
if a // 10 = 8:
    answer += 'восемьдесят '
if a // 10 = 9:
    answer += 'девяносто '


if a == 0:
    answer = answer + 'нуль' # answer += 'нуль'
elif a % 10 == 1:
    answer = answer + 'один'
elif a % 10 == 2:
    answer = answer + 'два'
elif a % 10 == 3:
    answer = answer + 'три'
elif a % 10 == 4:
    answer = answer + 'четыре'
elif a % 10 == 5:
    answer = answer + 'пять'
elif a % 10 == 6:
    answer = answer + 'шесть'
elif a % 10 == 7:
    answer = answer + 'семь'
elif a % 10 == 8:
    answer = answer + 'восемь'
elif a % 10 == 9:
    answer = answer + 'девять'
elif a == 10:
    answer = answer + 'десять'
elif a == 11:
    answer = answer + 'одиннадцать'
elif a == 12:
    answer = answer + 'двенадцать'
elif a == 13:
    answer = answer + 'тринадцать'
elif a == 14:
    answer = answer + 'четырнадцать'
elif a == 15:
    answer = answer + 'пятнадцать'
elif a == 16:
    answer = answer + 'шестнадцать'
elif a == 17:
    answer = answer + 'семнадцать'
elif a == 18:
    answer = answer + 'восемнадцать'
elif a == 19:
    answer = answer + 'девятнадцать'

print('Ваше число: ', answer)