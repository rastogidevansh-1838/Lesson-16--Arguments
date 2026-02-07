def factorial(x):
    '''this is a recursive function to find a factorial of a integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The facorial of 0:", factorial(0))
print("The facorial of 1:", factorial(1))
print("The facorial of 2:", factorial(4))
print("The facorial of 5:", factorial(5))
print("The facorial of 10:", factorial(10))