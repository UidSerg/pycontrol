from os import path
import datetime

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def show_all():
    """Вывод списка контактов"""
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")

def add_contact():
    """Добавляем заметку в конце списка"""
    note = input("Введите текст заметки:")
    with open(file_base, "a", encoding="utf-8") as f:
        if note:
            f.write(f'{last_id+1} {note} {datetime.datetime.today()}\n')

def search_func(book: list, poisk: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    return list(filter(lambda notes: poisk.lower() in notes.lower(), book))

def find_data() -> None:
    """вывод заметки."""
    object_search = input("введите данные для поиска:  ")
    result = search_func(all_data, object_search)
    count = len(result)
    if count == 0:
        print('Ничего не найдено по вашему запросу')
    else:
        for i in range(len(result)):
            print(result[i])

def change():
    """Изменение контакта"""
    object_search = input("введите данные для поиска:  ")
    result = search_func(all_data, object_search)
    count = len(result)
    if count == 0:
        print('Ничего не найдено по вашему запросу')
    elif count == 1:
        start = int(result[0].split()[0])
    elif count > 1:
        for i in range(count):
            print(f'{i+1}.[{result[i]}]')
        while True:
            new_search = int(input("Уточните какой контакт хотите изменить?: "))
            if new_search > 0 and count+1 > new_search:
                print(f'Изменяем [{result[new_search-1]}]')
                start = int(result[new_search-1].split()[0])
                break
            else:
                print("Указано неверноe значение для редактирования") 
                continue

        note = input("Введите текст заметки:")
        all_data[start-1] = str(f'{all_data[start-1].split()[0]} {note} {datetime.datetime.today()}')
        with open(file_base, 'w', encoding='utf-8') as f:
            for i in range(len(all_data)):
                with open(file_base, 'a', encoding='utf-8') as f:
                    f.write(f'{all_data[i]}\n') 
            print(f'Запись Изменена!')

def delete_contact():
    '''Удаление контакта''' 
    object_search = input("Введите что удаляем?: ")
    result = search_func(all_data, object_search)
    count = len(result)
    if count == 0:
        print('Ничего не найдено!')
    elif count == 1:
        start = int(result[0].split()[0])
        del_func(start, all_data)
    elif count > 1:
        for i in range(count):
            print(f'{i+1}.[{result[i]}]')
        while True:
            new_search = int(input("Уточните какой контакт хотите удалить?: "))
            if new_search > 0 and count+1 > new_search:
                print(f'Удаляем [{result[new_search-1]}]')
                start = int(result[new_search-1].split()[0])
                del_func(start, all_data)
                break
            else:
                print("Указано неверноe значение для удаления") 
                continue               

def del_func(start: int, all_data: list):
    """удаление"""        
    with open(file_base, 'w', encoding='utf-8') as f:
        for i in range(start-1):
            with open(file_base, 'a', encoding='utf-8') as f:
                f.write(f'{all_data[i]}\n') 
    for i in range(start, len(all_data)):
        with open(file_base, 'a', encoding='utf-8') as f:
            numeric=int(all_data[i].split()[0])
            line= str(all_data[i])
            srez = line[len(str(numeric)):] 
            srez = str(numeric-1)+srez
            f.write(f'{srez}\n')
    print(f'Удалено!!!')  

