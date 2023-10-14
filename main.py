class Stack:

  def __init__(self, stack_list: list, element: str = ''):
    self.stack_list = stack_list
    self.element = element

  def is_empty(self):
    return bool(self.stack_list)

  def push(self):
    if self.element != '':
      self.stack_list.append(self.element)

  def pop(self):
    return self.stack_list.pop()

  def peek(self):
    return self.stack_list[-1]

  def size(self):
    return len(self.stack_list)


parentheses = [
  '(((([{}]))))',
  '[([])((([[[]]])))]{()}',
  '{{[(])]}}',
  '}{}'
]
open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(parentheses: str) -> str:
  stack = []
  for i in parentheses:
    if i in open_list:
      Stack(stack, i).push()
    elif i in close_list:
      pos = close_list.index(i)
      if (((Stack(stack, i).size()) > 0) and 
        (open_list[pos] == stack[(Stack(stack, i).size())-1])):
        Stack(stack, i).pop()
      else:
        return print('Несбалансированно')
  if Stack(stack).size() == 0:
    return print('Сбалансированно')
  else:
    return print('Несбалансированно')

for par in parentheses:
  check(par)
