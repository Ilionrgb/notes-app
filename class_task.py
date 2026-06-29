import json
class Task:
    def __init__(self, title):
        self.title=title
        self.done=False
    def complete(self):
        self.done=True
    def show(self):
        if self.done:
            print(f'[x] {self.title}')
        else:
            print(f'[ ] {self.title}')
class TodoManager:
    def __init__(self):
        self.tasks=[]
    def add_task(self, title):
        task=Task(title)
        self.tasks.append(task)
    def complete_task(self, number):
        self.tasks[number-1].complete()
    def show_all(self):
        for i, task in enumerate(self.tasks ,start = 1):
            print(f'{i}:', end=" ")
            task.show()
    def save(self, filename):
        data = [{"title": task.title, "done": task.done} for task in self.tasks]
        with open(filename,"w") as f:
            json.dump(data,f)
    def load(self, filename):
        with open(filename, "r") as f:
            data=json.load(f)
        self.tasks = []
        for item in data:
            task = Task(item["title"])
            if item["done"]:
                task.complete()
            self.tasks.append(task)
manager = TodoManager()
try:
    manager.load("tasks.json")
except FileNotFoundError:
    pass
while(True):
    choose=int(input())
    if(choose==1):
        manager.show_all()
    elif(choose==2):
        title=input()
        manager.add_task(title)
    elif(choose==3):
        number=int(input())
        manager.complete_task(number)
    elif(choose==4):
        manager.save("tasks.json")
        break