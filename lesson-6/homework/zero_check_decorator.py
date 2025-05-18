def div(a, b):
   return a / b

try:
    print(div(6,0))
except ZeroDivisionError:
    print("Denominator can't be zero")
except:
    print("Input is not int")
