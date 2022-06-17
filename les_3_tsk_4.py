user_str = str(input('Введите число(минимум трехзначное) или слово'))
i = 0
while i < len(user_str):
    if user_str[i] == user_str[-i-1]:
        i += 1
        print('Это палиндром')
    else:
        print('Это не палиндром')
        break
    