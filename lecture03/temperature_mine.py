temperature = input("Введите температуру (последний символ должен быть шкалой (C,F): ")
list_temperature = list(temperature)

char_last = list_temperature[-1]
listscale = list('cCfF')
if not char_last in listscale : 
    print ("Непонятно, какую шкалу Вы используете")
    exit()

listnumber = list('+-0123456789')
list_temperature.del([-1])
for num_temperature in list_temperature:
    if not num_temperature in listnumber : 
        print ("Вы ввели неверное значение")
        exit()

temperature = float(temperature[0:-1])
if char_last in "Ff" :
    cel = (temperature-32)/1.8
    print ("Результат:", round((cel), 2), "C")
    button = input("Для продолжения нажмите Enter!")
elif char_last in "C" :
    far = temperature*1.8+32
    print ("Результат:", round((far), 2), "F")
    button = input("Для продолжения нажмите Enter!")