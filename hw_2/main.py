import re
import csv


# Читаем адресную книгу в формате CSV в список contacts.
def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts = list(rows)
    return contacts

# Помещаем Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
def fix_initials(contacts_list):
    contacts_list_upd =[]
    for contact in contacts_list:
        pattern = r'[\s,]'
        item_list = []
        for item in contact[:3]:
            result = re.split(pattern, item)
            item_list.extend(result)
            del(item_list[3:])
        del(contact[:3])
        item_list.extend(contact)
        contacts_list_upd.append(item_list)
    return contacts_list_upd

# Приводим все телефоны в формат +7(999)999-99-99/ +7(999)999-99-99 доб.9999
def fix_phones(contacts_list):
    contacts_list_upd = []
    for contact in contacts_list:
        pattern_1 = r'(\+7|8)?\s*\(?(\d{3})\)?\s*(\d{3})\-*(\d+)\-*(\d+)\s?\(?[доб\.\s]+(\d{4})?\)?'
        pattern_2 = r'(\+7|8)?\s*\(?(\d{3})\)?\-?\s*(\d{3})\-?(\d{2})\-?(\d+)'
        
        phone_exist_1 = re.search(pattern_1, contact[-2])    
        phone_exist_2 = re.search(pattern_2, contact[-2])    
        if phone_exist_1 is not None:
            result = re.sub(pattern_1, r'+7(\2)\3-\4-\5 доб.\6', contact[-2])
            contact[-2] = result
        elif phone_exist_2 is not None:
            result = re.sub(pattern_2, r'+7(\2)\3-\4-\5', contact[-2])
            contact[-2] = result
        
        contacts_list_upd.append(contact)
    return contacts_list_upd

# Объединияем все дублирующиеся записи о человеке в одну.
def merge_double_recordes(contacts_list):
    contacts_to_del = []    
    for contact in contacts_list:
        pattern = ', '.join([contact[0], (contact[1])])
        start_slice = contacts_list.index(contact) + 1 
        for element in contacts_list[start_slice:]:
            full_name = ', '.join([element[0], (element[1])])
            result = re.search(pattern, full_name)
            if result is not None:
                if contact[2] == '':
                    contact[2] = element[2]
                if contact[3] == '':
                    contact[3] = element[3]
                if contact[4] == '':
                    contact[4] = element[4]
                if contact[5] == '':
                    contact[5] = element[5]
                if contact[6] == '':
                    contact[6] = element[6]
                contacts_to_del.append(element)
    contacts = [contact for contact in contacts_list if contact not in contacts_to_del]
    return contacts

# Сохраняем получившиеся данные в другой файл.
def write_to_file(contacts_list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    address_book = read_file('phonebook_raw.csv')
    address_book = fix_initials(address_book)
    address_book = fix_phones(address_book)
    address_book = merge_double_recordes(address_book)
    write_to_file(address_book)