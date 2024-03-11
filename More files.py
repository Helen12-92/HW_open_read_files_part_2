import os

folder_way = r'C:\Users\79526\OneDrive\Рабочий стол\Нетология\ДЗ\Открытие и чтение файла\Чтение разных файлов\Разные файлы\files'

every_files = os.listdir(folder_way)
file_list = []

for file in every_files:
    with open(f'{folder_way}/{file}','r',encoding="utf8") as f:
        file_line = f.readlines()
        file_list.append([str(len(file_line)),file, file_line])

file_list.sort()
for x in file_list:
    x[0], x[1] = x[1], x[0]

with open('all_files.txt', 'a', encoding="utf8") as f:
    for list_ in file_list:
        for i in list_:
            f.writelines(i)
            f.write('\n')
        f.write('\n')