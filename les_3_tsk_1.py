a=int(input('Введите целое число, которое больше 0 и меньше 10: '))
while True:
    if 0<a<10:
        print('a=',a*5)
        break
    else:
        print('Число должно быть больше нуля и меньше десяти!')
        a = int(input('Введите целое число, которое больше 0 и меньше 10: '))