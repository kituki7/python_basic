user_str = str(input('Введите любой небольшой текст:\n'))
up = 0
low = 0
i = 0
upper = None
while i < len(user_str):
    sym=user_str[i]
    upper = sym.isupper()
    if upper == True:
        up+=1
    elif sym.isdigit():
        None
    elif upper == False:
        low+=1
    i+=1
print(f'Кол-во символов в  строке: {len(user_str)}')
print(f'Кол-во прописных символов: {up}')
print(f'Кол-во строчных символов: {low}')