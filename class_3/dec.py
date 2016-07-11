def only_int_arguments(f):
    print("Entering decorator...")
    def new_f(a, b):
        print("Entering new_f...")
        if type(a) != int or type(b) != int:
            raise ValueError("Only int arguments!")
        print("Check is OK! Both ints. Invoking f: {}".format(f))
        f(a, b)
        print("f was just invoked")
    return new_f


@only_int_arguments
def add(a, b):
    print(" ===== ACTUAL SUM =====")
    print(a + b)


add(2, 3)
