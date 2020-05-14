"""
The below decorator converts the functions output to lowercase.
"""


def lower_case(f):
    """A decorator function that takes in a function and returns a function"""
    def lf(*args, **kwargs):
        """
            Local function that takes in args, kwargs and calls in the function f with those arguments.
            It then converts the output of f to lower case and returns the output
        """
        x = f(*args, **kwargs)
        return x if x == None else str(x).lower()

    return lf


@lower_case
def say_hello():
    return "Hello World!!!"

@lower_case
def say_hello2(name):
    return f"Hello {name}!!!"

print(say_hello())

print(say_hello2("John"))
