# Todos
  # - Show all todos
  # - Show active Todos # - Show completed Todos
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

  def show_todo(self, id):
    """This method will get the todo which matches the id"""
    todo = self._find(id)
    self._formatted_todo_text(todo)

  def show_all_todos(self, todos={}):
    for todo in todos if todos else self.todo_items:
      item = self.todo_items[todo]
      self._formatted_todo_text(item)
    
  def delete_todo(self, id):
    """This item will delete a todo from the dictionary 
    which matches the given id"""
    self.todo_items.pop(id)

  def mark_complete(self, id):
    """This function will mark a todo as completed.
    Again there is an issue when any todo with that id doesn't exist"""
    todo = self.todo_items.get(id)
    todo.status = 'Completed'

  def find_items_by_status(self,  value):
    """This function will find all todos  by status"""
    def callback(id):
      if(self.todo_items[id].status == value): 
        return True    

    result = filter(callback, self.todo_items)
    result = list(result)

    if len(result) > 0:
      for item in result  :
        self._formatted_todo_text(self.todo_items[item])
    else:
      print("No todos found")


  def _find(self, id):
    """This function will find todo but its id."""
    for todo in self.todo_items.keys():
      if(int(id) == int(todo)):
          return self.todo_items[id]


  def _formatted_todo_text(self, todo):
    print("""
Id: {id}
Todo: {text}
Created: {creation_date}
Status: {status}
Due Date: {due_date}
--------------------------------""".format(id=todo.id,text=todo.text, creation_date=todo.creation_date, status=todo.status, due_date=todo.due_date))

if __name__ == "__main__":
  todos = Todos()

  todos.add_todo("Buy milk")
  todos.add_todo("Buy eggs")
  todos.delete_todo(1)
  todos.show_all_todos() 
  todos.mark_complete(2)
  todos.show_all_todos()
