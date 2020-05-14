import functools

"""
Demonstrates how multiple decorators are called
"""

def lower_case(f):
    """A decorator function that takes in a function and returns a function"""
    @functools.wraps(f) # We do this to ensure the properties of wrapped function remains
    def lf(*args, **kwargs):
        """
            Local function that takes in args, kwargs and calls in the function f with those arguments.
            It then converts the output of f to lower case and returns the output
        """
        x = f(*args, **kwargs)
        return x if x == None else str(x).lower()

    return lf


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if(self.enabled):
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap


trace = Trace()


@trace
@lower_case
def say_hello():
    return "Hello World!!!"

@trace
@lower_case
def say_hello2(name):
    return f"Hello {name}!!!"

print(say_hello())

trace.enabled = False
print(say_hello2("John"))

trace.enabled = True
print(say_hello2("Manish"))

