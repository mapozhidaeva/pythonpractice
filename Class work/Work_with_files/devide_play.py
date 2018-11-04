# открыть файл для чтения

# how to work with files:
# https://www.guru99.com/reading-and-writing-files-in-python.html


import re
import os

path = '/Users/Marina/PycharmProjects/pythonpractice/Class work'

with open('Zoikina_kv.txt') as f:
    play = f.read().split('\n')


# написать регулярки для деления на части
# пример: a = re.findall('[a-zA-Zа-яА-ЯёЁ]+\-[1-9]+', china)
# re.search('<+', s)
act = '^(АКТ).+$'
pic = '^(КАРТИНА)(.+)$'
for i in play:
    if (bool(re.search(act, i))) == True:
        if not os.path.exists(str(i)):
            os.mkdir(str(i))
            dirname = str(i)
    elif (bool(re.search(pic, i))) == True:
        a = str(i)
        open(str(i + '.txt'), 'w')



        print (i)




# создать папки для частей и файлы для картин
# записать их туда

