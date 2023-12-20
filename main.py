import json
from datetime import datetime

notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, default=str)

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    now = datetime.now().isoformat()
    notes.append({'id': len(notes)+1, 'title': title, 'body': body, 'timestamp': now})
    save_notes()
    print('Заметка успешно сохранена')

def read_notes(filter_date=None):
    if filter_date:
        filtered = [note for note in notes if filter_date in note['timestamp']]
        for note in filtered:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}, Дата: {note['timestamp'][:10]}")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}, Дата: {note['timestamp'][:10]}")

def edit_note():
    id = int(input('Введите ID заметки для редактирования: '))
    for note in notes:
        if note['id'] == id:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новое тело заметки: ')
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.now().isoformat()
            save_notes()
            print('Заметка успешно отредактирована')
            return
    print('Заметка с указанным ID не найдена')

def delete_note():
    id = int(input('Введите ID заметки для удаления: '))
    global notes
    notes = [note for note in notes if note['id'] != id]
    save_notes()
    print('Заметка успешно удалена')

def main():
    global notes
    notes = load_notes()
    while True:
        command = input('Введите команду (1 - добавить, 2 - вывести все заметки, 3 - найти заметку по дате , 4 - изменить заметку, 5 - удалить заметку, 0 - выйти): ')
        if command == '1':
            add_note()
        elif command == '2':
            read_notes()
        elif command == '3':
            filter_date = input('Введите дату для фильтрации (YYYY-MM-DD): ')
            read_notes(filter_date)        
        elif command == '4':
            edit_note()
        elif command == '5':
            delete_note()
        elif command == '0':
            break
        else:
            print('Неправильная команда')

if __name__ == '__main__':
    main()