"""
Todo class 
"""
import datetime



class Todo:
  STATES = {'in_process': 'in_process', 'complete': 'complete'}
  def __init__(self, title, due_date, description):
    self.title = title
    self.creation_date = datetime.datetime.now()
    self.due_date = due_date
    self.description = description
    self.category = []
    self.state = self.STATES['in_process']
    
  def add_category(self, category):
    self.category.append(category)
  
  def complete_todo(self):
    self.state = self.STATES['complete']
    return self.state
