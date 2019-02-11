import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
new_list = []
new_list.append(contacts_list[0])
for note in contacts_list[1:]:
    correct_record = []
    #Разбивка и правильная сборка ФИО
    for part_full_name in re.findall(r'\w+', ' '.join(note[:3])):
        correct_record.append(part_full_name)

    #Добавление organization
    correct_record.append(note[3])

    #Добавление position
    correct_record.append(note[4])

    #Обработка и добавление телефона
    phone_raw = re.findall(r'[7-8]\s*\(*\d*[\)\-\s]*\d*\-*\d*\-*\d{2}', note[5])
    if len(phone_raw) > 0:
        phone_clear = re.sub(r'\s*\(*\)*\-*', '', phone_raw[0])
        phone = f'+7({phone_clear[1:4]}){phone_clear[4:7]}-{phone_clear[7:9]}-{phone_clear[9:]}'
        if re.findall(r'доб\.', note[5]):
            prefix = re.findall(r'доб\.\s*\d+', note[5])[0][-4:]
            phone += f' доб.{prefix}'
        correct_record.append(phone)

    # Добавление email
    correct_record.append(note[6])



    new_list.append(correct_record)


n = len(new_list)
for i in range(n):
    for j in range(i+1, n):
        if new_list[i][:3] == new_list[j][:3]:
            print(new_list[i])
            print(new_list[j])




# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_list)
