def func():
    while type:
        print ('че в че переводим: ', end = '')
        getchar=input()
        try:
            if getchar in 'cC':
                print ('Введи температуру в градусах Цельсия: ', end = '')
                getTempNumber=input ()
                getTempNumber=float(getTempNumber)
                print(getTempNumber, " градусов Цельсия =  ", round((getTempNumber * 1.8) + 32, 3)," градусов Фаренгейт.")
            elif getchar in 'Ff':
                print ('Введи температуру в градусах Цельсия: ', end = '')
                getTempNumber=input ()
                getTempNumber=float(getTempNumber)
                print(getTempNumber, " градусов Фаренгейт =  ", round((getTempNumber -32) / 1.8, 3)," градусов Цельсия.")
            else: 
                print("непонятно")
        except ValueError:
            print ('"'+  getTempNumber + '"' + ' - не является числом')
        else:
            print("Продолжить? y/n", end = '')
            getchar = input()
            if getchar == 'y':
                func()
            elif getchar == 'n':
                exit()
func() 



