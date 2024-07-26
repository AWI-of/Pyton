from date_cerate import*

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_phone()
    phone = input_phone()
    address = input_adress()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'
def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf=8') as file:
        file.write(contact_str)
        def print_contacts():
            with open("phonebook.txt", 'r', encoding='utf-8') as file:
                contact_str = file.read()
                contact_list = contact_str.rstrip().split('\n\n')
                for n, contact in enumerate(contact_list, 1):
                    print(n, contract)
                    def search_contact():
                        print(
                            'возможные варианты поиска:\n'
                            '1. По фамилии\n'
                            '2. По имени\n'
                            '3. По телефону\n'
                            '4. По отчеству\n'
                            '5. По адресу(городу)'
                        )
var = input('Выберете вариант поиска: ')
while var not in ('1', '2', '3', '4', '5'):
