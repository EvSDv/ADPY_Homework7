import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
new_list = []
for note in contacts_list[1:]:
    correct_record = []
    #Разбивка и правильная сборка ФИО
    for part_full_name in re.findall(r'\w+', ' '.join(note[:3])):
        correct_record.append(part_full_name)

    #Добавление organization
    correct_record.append(note[3])

    #Добавление position
    correct_record.append(note[4])

    #Обработка и жобавление телефона
    correct_record.append(note[5])


    a = re.findall(r'[7-8]\s*\(*\d*[\)\-\s]*\d*\-*\d*\-*\d{2}', note[5])
    if len(a) > 0:
        line = re.sub(r'\s*\(*\)*\-*', '', a[0])
        print(line)



    new_list.append(correct_record)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_list)