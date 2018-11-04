
# ПЕРЕВОД в бинарное кодирование
num = 8
print (f"Binary: {num:#b}")
# 'Binary: 0b1000'

# СТРОЧКИ F
num = 2 / 3
print(num)
print(f"{num:.3f}")
#0.6666666666666666
#0.667


example_string = "привет"
print(type(example_string))
print(example_string)
# <class 'str'>
# привет
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))
# b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
# <class 'bytes'>

# Декодируем байты обратно в строку:
decoded_string = encoded_string.decode()
print(decoded_string)
# привет

import random

number = random.randint(0, 100)



while True:
    answer = input('Угадайте число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введите правильное число")
        continue

    answer = int(answer)

    if answer == number:
        print('Совершенно верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
