import json
import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note.__dict__)
        self._save_notes()

    def edit_note_title(self, index, new_title):
        self.notes[index]['title'] = new_title
        self._save_notes()

    def edit_note_content(self, index, new_content):
        self.notes[index]['content'] = new_content
        self._save_notes()

    def delete_note(self, index):
        del self.notes[index]
        self._save_notes()

    def get_notes(self):
        return [Note(note['title'], note['content']) for note in self.notes]

    def _save_notes(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    file_path = 'notes.json'
    manager = NoteManager(file_path)

    while True:
        print("""
        1. Добавить заметку
        2. Редактировать заметку
        3. Удалить заметку
        4. Отобразить все заметки
        5. Выйти
        """)

        choice = input("Введите команду: ")

        if choice == '1':
            title = input("Введите название заметки: ")
            content = input("Введите текст заметки: ")
            manager.add_note(title, content)

        elif choice == '2':
            print("Список заметок:")
            for i, note in enumerate(manager.get_notes()):
                print(f"{i + 1}. {note.title}")

            index = int(input("Введите номер заметки для редактирования: ")) - 1
            title_or_content = input("Что вы хотите отредактировать (название или содержимое)? ")

            if title_or_content.lower() == 'название':
                new_title = input("Введите новое название: ")
                manager.edit_note_title(index, new_title)
            elif title_or_content.lower() == 'содержимое':
                new_content = input("Введите новое содержимое: ")
                manager.edit_note_content(index, new_content)

        elif choice == '3':
            print("Список заметок:")
            for i, note in enumerate(manager.get_notes()):
                print(f"{i + 1}. {note.title}")

            index = int(input("Введите номер заметки для удаления: ")) - 1
            manager.delete_note(index)

        elif choice == '4':
            print("Все заметки:")
            for i, note in enumerate(manager.get_notes()):
                print(f"{i + 1}. {note.title} - {note.content}")

        elif choice == '5':
            break

