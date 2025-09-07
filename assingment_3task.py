 # task 1

def factorial(n):
     if n==0 or n==1:
         return 1
     else:
         return n*(factorial(n-1))
print("factorial of 5 is :", factorial(5))

# task 2

import math
num = float(input("enter the number : "))
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.radians(num)
print("square root : ",sqrt_val)
print("logarithm : ",log_val)
print("sine : ",sine_val)
