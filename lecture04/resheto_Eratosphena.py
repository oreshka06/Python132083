try:
    num = int(input('Введите число: '))
except ValueError:
    print('Некорректный ввод данных')
    btwn = input()
    exit()
numberlist = list(range(2, num + 1 ))
for i in range(2, len(numberlist)+2):
    if i*i <= num:
        if str(numberlist[i-2]).isdigit() == True:
            j = i*i
            count = 1
            while j <= len(numberlist)+1: 
                numberlist[j-2] = '!'
                j = i*i + count * i
                count += 1            
for i in range(2, len(numberlist)+2):
    if str(numberlist[i-2]).isdigit() == True:
        print(i)
btwn = input()
