form longger import*

def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass
    var = 0
    while var != '4':
        print(
'Возможные варианты:\n'
'1. Добавить контакт\n'
'2. Вывести на экран\n'
'3. Поиск контакта\n'
'2. Выход\n'
        )
        print()
        match var:
            case '1':
                add_contact()
                case '2':
                print_contacts()
                case '3':
                search_contact()
                case '4':
                 print('До свидания!')
                print()
