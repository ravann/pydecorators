

def operate_mult(x, y):
    """Multiply operator function"""
    return x * y

def operate_div(x, y):
    return x / y

def operate_plus(x, y):
    return x + y

def operate_minus(x, y):
    return x - y

z = operate_mult(5, 4)
print(z)
z = operate_div(5, 4)
print(z)
z = operate_plus(5, 4)
print(z)
z = operate_minus(5, 4)
print(z)

def operate(operate_func, *args):
    """ A variable operator function that takes in the operator function and numbers and inturn call the operator function """
    z = operate_func(*args)
    print(f"Output of {str(operate_func)} with inputs {args} is : {z}")


operate(operate_minus, 5, 4)

# We can also send in a lambda function to the operate
operate( lambda x, y: x % y, 5, 4  )

