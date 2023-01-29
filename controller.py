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
                pass
            case 6:
                pass
            case 7:
                find = v.find_contact()
                result = m.search_contact(find)
                v.show_contacts(result)
            case _:
                v.input_error()
     

