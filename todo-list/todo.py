# Todo
  # - Todo will contian
    # - Text
    # - Creation Date
    # - Status
    # - Due Date
    # - Change Todo Text
    # - Change Todo Status
    # - Change Due Date
from datetime import date

last_id = 0

class Todo:
  def __init__(self, text, due_date=""):
    self.text = text
    self.creation_date = date.today()
    self.status = 'Incomplete'
    self.due_date = due_date
    global last_id 
    last_id += 1
    self.id = last_id
