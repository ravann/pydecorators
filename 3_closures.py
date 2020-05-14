
"""
Everytime the raise_2_power is called, a new function is created.
The variables this function uses from the parent function are kept by the local function.
"""

def raise_2_power(exp):
    """Returns the function that raises the given argument to the nth power"""
    def lf(n):
        return n ** exp
    return lf

square = raise_2_power(2) # We just need to define this once and can call it multuple times.
# The function lf will keep the value exp and will not let it garbage collected
# This concept is called closures
print(square(4))

cube = raise_2_power(3)
print(cube(4))

