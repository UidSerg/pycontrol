import func

def main_menu():
    play = True
    while play:
        func.read_records()
        answer = input("Заметки:\n"
                       "1. Показать все заметки\n"
                       "2. Добавить заметку\n"
                       "3. Поиск заметки\n"
                       "4. Изменить заметку\n"
                       "5. Delete\n"
                       "6. Exit\n")
        match answer:
            case "1":
                func.show_all()
            case "2":
                func.add_contact()
            case "3":
                func.find_data()           
            case "4":
                func.change()
            case "5":
                func.delete_contact()
            case "6":
                play = False
            case _:
                print("Не известная команда, повторите ввод \n")

main_menu()