# Todos
  # - Show all todos
  # - Show active Todos
  # - Show completed Todos
  # - Show incomplete Todos
  # - Add new Todo
  # - Delete Todo
  # - Update Todo
  # - Mark Todo Complete

from todo import Todo


class Todos:
  def __init__(self):
    self.todo_items = {}

  
  def add_todo(self, text, due_date=""):
    """This function will add a new todo"""
    todo = Todo(text, due_date)
    self.todo_items.update({todo.id: todo})

  
  def show_all_todos(self):

    for todo in self.todo_items.keys():
      print(self.todo_items[todo].text)


if __name__ == "__main__":
  todos = Todos()

  todos.add_todo("Buy milk")
  todos.add_todo("Buy eggs")

  todos.show_all_todos()
