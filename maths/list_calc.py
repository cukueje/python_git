def addition(*args):
  sum = 0
  for i in args:
    sum += i
  return sum

def substraction(*args):
  if args is None:
    return 0
  sum = args[0] 
  for i in args[1:]:  
    sum -= i
  return sum

def __init__(leopard):
    super().__init__()
  def num_legs(leopard):
    return 4
  def talk(leopard):
    return ''
  def color(leopard):
    return 'brown' ' ' 'and' ' ' 'black'