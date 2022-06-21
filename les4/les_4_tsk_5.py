n = int(input('Введите целое число от 3 до 20: '))
d = (input(f'Введите {n}  чисел'))
d.split()
s = d.values()
def my_sum(a, b):
    c = a + b
    return c

res = my_sum(s, 0)
print(res//n)