def first_n_integers(n=10):
    i = 0
    while i < n:
        print("Before yield")
        yield i
        print("After yield")
        i += 1

    print("\nIteration finished")
    # raise StopIteration()

it = first_n_integers(2)
for num in it:
    print(num)
