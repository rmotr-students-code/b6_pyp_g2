class count_calls(object):

    func_calls = {}

    def __init__(self, func):
        self.func = func
        self._counter = 0

    def counter(self):
        return self._counter
        
    def counters(self):
        return self.func_calls
        
    def print_something(self):
        print(self.my_name)
    
    def __call__(self, *args, **kwargs):
        #print("__call__")
        self._counter += 1
        return self.func(*args, **kwargs)
        

@count_calls
def my_func():
    print("My func")
print(my_func.counter())
my_func()
my_func()

print(my_func.counter())