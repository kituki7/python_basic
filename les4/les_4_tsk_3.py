first = int(input('Введите целое число'))
sec = int(input('Введите целое число'))
third = int(input('Введите целое число'))
if first > sec:
    if first > third:
        print(first)
    else:
        print(third)
else:
    if sec > third:
        print(sec)
    else:
        print(third)