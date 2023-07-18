def greetings():
    print ('Привет!')

def menu():
    print(
'''1 - Показать все заметки
2 - Добавить заметку
3 - Поиск
4 - Изменить заметку
5 - Удалить заметку
6 - Выход'''
)

def show_contacts(self):
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    print('\n')
    print (content)
    print('\n')


def success(self):
    print('\n')
    print ('Не удалось добавить заметку')
    print('\n')

def not_success(self):
    print('\n')
    print ('Заметка добавлена')
    print('\n')

def error():
    print('\n')
    print ('Ошибка ввода')
    print('\n')