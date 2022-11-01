# Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args,**kwargs):
    print( f" Called function is {function.__name__}{args}")
    result=function(args[0],args[1])
    print( f"it returned {result}")
  return wrapper

# Use the decorator 👇
@logging_decorator
def sum(a, b):
  return a+b
sum(2,4)

@logging_decorator
def prod(a,b):
  return a*b
prod(50,30)