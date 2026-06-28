import json
class Note:
    def __init__(self,title,content):
        self.title=title
        self.content=content
    def show(self):
        print(f'Заголовок: {self.title}')
        print(f'Текст: {self.content}')
class NoteManager:
    def __init__(self):
        self.notes=[]
    def add_note(self,title,content):
        note = Note(title, content)
        self.notes.append(note)
    def show_all(self):
        for i, note in enumerate(self.notes, start=1):
            print(f'{i}. {note.title}')
    def delete_note(self, number):
        self.notes.pop(number-1)
    def save(self, filename):
        data = [{"title": note.title, "content": note.content} for note in self.notes]
        with open(filename,"w") as f:
            json.dump(data,f)
    def load(self, filename):
        with open(filename,"r") as f:
            data=json.load(f)
        self.notes = [Note(item["title"], item["content"]) for item in data]
manager = NoteManager()
try:
    manager.load("notes.json")
except FileNotFoundError:
    pass
while True:
    print("\n1. Показать все\n2. Добавить\n3. Удалить\n4. Выход")
    choice = input("Выбери: ")
    if choice == "1":
        manager.show_all()
    elif choice == "2":
        title=input()
        content=input()
        manager.add_note(title,content)
    elif choice == "3":
        number=int(input())
        manager.delete_note(number)
    elif choice == "4":
        manager.save("notes.json")
        break