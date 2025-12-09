import math

#Basic operations: addition, subtraction, multiplication and division

#Adds a to b
def add(a, b):
  return a + b

#Subtracts b from a
def sub(a, b):
  return a - b

#Multiplies a and b together
def mult(a, b):
  return a * b

#Divides b from a
def div(a, b):
  if (b == 0):
    return "N/A"
  else:
    return a / b

#Advance operations: log, square, sin, cos, square root, percentage. Think of boundary conditions

#Logs a number and determines base
def log(a, b=10):
  if (b != 10):
    return math.log10(a)
  else:
    return math.log(a, b)
  
#Squares a number
def square(a):
  return a ** 2

#Applies the sin to a number
def sin(a):
  return math.sin(a)

#Applies the cos to a number
def cos(a):
  return math.cos(a)

#Square roots a number
def sqrt(a):
  if (a >= 0):
    return math.sqrt(a)
  else:
    return "N/A"

#Makes a number a percentage
def perc(a):
  return str(a * 100) + "%"
