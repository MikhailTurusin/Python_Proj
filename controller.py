import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input ('Введите команду: ')
        if answer == '1':
            date = model.get_data()
            view.show_contacts(date)
        elif answer == '2':
            contact = input('Введите заметку через пробел: ')
            res = model.add_contact(contact)
            if res:
                view.success(res)
            else:
                view.not_success(res)
        elif answer == '3':
            contact = input ('Введите данные из заметки для поиска: ')
            result = model.find(contact)
        elif answer == '4':
            contact = input ('Введите данные заметки для внесения изменений: ')
            result = model.change(contact)
        elif answer == '5':
            contact = input ('Введите данные заметки для удаления: ')
            result = model.delete(contact)
        elif answer == '6':
            break
        else:
            view.error()