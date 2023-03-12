from pprint import pprint
import re

## Читаем адресную книгу в формате CSV в список contacts_list:
import csv


with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код
name_pattern = r'^(\w+)(\s*)(\,?)(\w+)(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)'
phone_pattern = (
    r'(\+7|8)(\s*)(\(*)(\d{3})(\-*)(\)*)(\s*)(\d{3})(\-*)(\s*)'
    r'(\d{2})(\-*)(\s*)(\d{2})(\s*)(\(*)(доб\.)*(\s*)(\d+)*(\)*)'
)
name_replace = r'\1\3\10\4\6\9\7\8'
phone_replace = r'+7(\4)\8-\11-\14\15\17\19'

contacts_list_new = list()
for contacts in contacts_list:
    contact_string = ','.join(contacts)
    contact_edit = re.sub(phone_pattern, phone_replace, contact_string)
    contact = contact_edit.split(',')
    contacts_list_new.append(contact)

contacts_list_new2 = list()
for contacts in contacts_list_new:
    contact_string = ','.join(contacts)
    contact_edit = re.sub(name_pattern, name_replace, contact_string)
    contact = contact_edit.split(',')
    if len(contact) == 7:
        contacts_list_new2.append(contact)
    else:
        contact.pop()
        contacts_list_new2.append(contact)

for i in contacts_list_new2:
    for j in contacts_list_new2:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
        finish_list = list()
        for contacts in contacts_list_new2:
            if contacts not in finish_list:
                finish_list.append(contacts)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open('phonebook.csv', 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(finish_list)