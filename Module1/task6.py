def factorial(x):
    if(x>0):
        result = x*factorial(x-1)
          
    else:
        result = 1
    return result

print(factorial(5))