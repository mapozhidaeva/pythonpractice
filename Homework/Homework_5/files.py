'''Программа должна обходить всё дерево папок, начинающееся с той папки,
где она находится, и сообщать следующую информацию:

1. какова максимальная глубина папки в этом дереве (глубину папки с
программой нужно считать равной 0);
2. сколько в дереве папок с полностью кириллическими названиями;
3. файлы с каким расширением чаще всего встречаются в этих папках
(если таких много, можно печатать только одно);
4. на какую букву начинается название большинства папок
(если таких много, можно печатать только одну);
5. сколько в этих папках встречается разных названий файлов без учёта расширений;
6. в скольких папках встречается несколько файлов с одним и тем же расширением;
7. в какой папке лежит больше всего файлов.

Всю информацию нужно записывать в текстовый файл рядом с самой программой.'''

import os
import re

filename = 'text.txt'

with open(filename, 'w') as f:
    f.write('')
# print (dir(os))
init_dir = os.getcwd()
n = '/Users/Marina/PycharmProjects/pythonpractice'
check_folder = set()



print (check_folder)
slash_count = n.count('/')
print (slash_count)
folders_with_same_extension = 0

# print (os.listdir())
# print (os.stat('Work_with_files'))
depth = 0
deepest_folder = ''
extension = {}
first_letter = {}
filenameset = set()
reg = '^[а-яА-Я ]+$'
names = []
filenumber = 0
biggest_folder = ''
folders_with_repeating_ext = 0

for dirpath, dirnames, filenames in os.walk(n):
    dirs = dirpath.strip('/').split('/')
    local_ext = {}
    # Посчитаем, сколько папок с полностью кириллическими названиями.
    # Для этого проверим на наличие во множестве
    # К сожеланию, код обрабатывает только уникальные имена, а не уникальные папки
    for d in dirs:
        if d not in check_folder:
            check_folder.add(d)
    #print (type(dirpath), type(dirnames), type(filenames))
    # print ('Current Path:', dirpath)
    c = dirpath.count('/') - slash_count
    if c > depth:
        depth = c
        deepest_folder = dirpath
    #print ('Directories:', dirnames)
    # print ('Files:', filenames)
    if len(filenames) > filenumber:
        filenumber = len(filenames)
        biggest_folder = dirpath

    for file in filenames:
        name_ext = file.strip('.').split('.')
        first = str(name_ext[0]).lower()

        f = first[0].lower()
        if f not in first_letter:
            first_letter[f] = 1
        else:
            first_letter[f] += 1
        if len(name_ext) > 1:
            filenameset.add(''.join([i for i in name_ext[:-1]]))
            e = name_ext[-1]
            if e not in extension:
                extension[e] = 1
            else:
                extension[e] += 1
            if e not in local_ext:
                local_ext[e] = 1
            else:
                local_ext[e] += 1
        else:
            filenameset.add(name_ext[0])

    if len(local_ext) > 0:
        print (local_ext)
        loc_ext_dic = max(local_ext, key=lambda x: local_ext[x])
        if local_ext[loc_ext_dic] > 1:
            folders_with_repeating_ext += 1

count_cyrrilis_folder_names = 0
# Сколько папок с кириллическими названиями
filenameset.add('прволи')
for i in list(check_folder):
    if re.match(reg, i):
        count_cyrrilis_folder_names += 1

if count_cyrrilis_folder_names == 0:
    count_cyrrilis_folder_names = 'нет'

most_frequent_ext = max(extension, key=lambda x: extension[x])
freq_first_let = max(first_letter, key=lambda x: first_letter[x])

the_output = '''
1. Максимальная глубина папки: {} 
2. Папок с полностью кириллическими названиями {}
3. Самое частотное расширение: {}
4. Большинство папок начинаются на букву "{}"
5. Уникальным названий файлов: {}
6. Папок, в которых встречаются файлы с одинаковым расширением: {}
7. Максимальное количество файлов в папке: {}
(в папке {})'''.format(depth, count_cyrrilis_folder_names, most_frequent_ext, freq_first_let,
                                    len(filenameset), folders_with_repeating_ext, filenumber, biggest_folder)

print (the_output)
def main():
    f = open('text.txt', 'w')
    f.write(the_output)
    f.close()
    return 0

if __name__ == '__main__':
    main()