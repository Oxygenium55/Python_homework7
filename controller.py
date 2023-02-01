import view as v
import model as m

def start():
    choice = ''
    while choice != 8:
        choice = v.main_menu()
        match choice:
            case 1:
                m.open_file()
            case 2:
                m.save_file()
            case 3:
                v.show_contacts(m.get_phone_book())
            case 4:
                new_contact = list(v.create_new_contact())
                m.add_new_contact(new_contact)
            case 5:
                del_name = v.select_contact('Введите удаляемый контакт: ')
                contact = m.get_contact(del_name)
                if contact:
                    confirm = v.delete_confirm(contact[0][0])
                    if confirm:
                        m.remove_contact(contact[0])
                elif contact == []:
                    v.empty_request()
                else:
                    v.many_request()
            case 6:
                name = v.select_contact('Введите имя изменяемого контакта: ')
                contact = m.get_contact(name)
                if contact:
                    changed = v.change_contact()
                    m.edit_contact(contact[1], list(changed))
                elif contact == []:
                    v.empty_request()
                else:
                    v.many_request()
            case 7:
                find = v.find_contact()
                result = m.search_contact(find)
                v.show_contacts(result)
            case 8:
                v.end_program()
                break
     

