while type:
    print ('Введи температуру в градусах Цельсия: ', end = '')
    getTempNumber=input ()
    try:
        getTempNumber=float(getTempNumber)
    except ValueError:
        print ('"'+  getTempNumber + '"' + ' - не является числом')
    else:
        break
print(getTempNumber, " градусов Цельсия =  ", round((getTempNumber * 1.8) + 32, 3)," градусов Фаренгейт.")
btwn = input("Для продолжения нажмите Enter!")
print('Hello')