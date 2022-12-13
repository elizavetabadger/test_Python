from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def Hello():
    print("Это телефонный справочник!")

def input_data():
    last_name = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    phone_number = input("Введите Телефон: ")
    description = input("Введите Описание: ")
    return [last_name, name, phone_number, description]

def choice():
    print("Что Вы хотите сделать?\n\
    1 - импорт\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        import_data(input_data())
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Телефон".center(20), "Описание".center(20))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данных нет")