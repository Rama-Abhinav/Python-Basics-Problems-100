#Handle division by zero.							

try:
 Div = 100/0
except ZeroDivisionError:
 print("Numbers cannot be divided by Zero as any number divided by zero is infinity")
