

class CallDemo():

    def __init__(self):
        return;

    def __call__(self, name, *args, **kwargs):
        """The call function makes the object callable.  This is call when the object is called."""
        print(f"Call function invoked ... with name : {name} ")


cd = CallDemo()
cd("Ravan") # Call the __call__ function

cd.__call__("Ravan")
