commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu() -> int:
    print('Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice
            else:
                print('Введите значение от 1 до 8')
        except ValueError:
            print('Введите корректное значение: ')

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:20} {contact[1]:13} {contact[2]:20}')
        print()

def input_error():
    print('Ошибка ввода. Введите корректный пункт меню')

def empty_request():
    print('Контакт не найден')

def many_request():
    print('Найдено более одного контакта. Уточните данные.')

def create_new_contact():
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    comment = input('Введите коммент: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

def change_contact():
    print('Введите новые данные. Если изменения не требуются, нажмите Enter')
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    comment = input('Введите коммент: ')
    return name, phone, comment

def delete_confirm(contact: str):
    result = input(f'Вы действительно хотите удалить контакт {contact}? (y/n)').lower()
    if result == 'y':
        return True
    else:
        return False

def end_program():
    print('Программа завершена. До новых встреч!')

