class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def display_info(self):
        print("Title:", self.title)
        print("Description:", self.description)
        print("Status:", "Completed" if self.completed else "Incomplete")

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_list(self):
        print("ToDo List:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.title} - {item.description} ({'Completed' if item.completed else 'Incomplete'})")

if __name__ == "__main__":
    todo_list = TodoList()

    todo_item1 = TodoItem("Complete Python project", "Finish coding and testing")
    todo_item2 = TodoItem("Buy groceries", "Milk, eggs, bread")
