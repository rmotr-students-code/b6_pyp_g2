class SimpleIterator(object):
    def __init__(self):
        self.times = 0

    def __iter__(self):
        return SimpleIterator()

    def __next__(self):
        if self.times == 3:
            raise StopIteration()
        self.times += 1
        return self.times

     next = __next__

it = SimpleIterator()

# it = it._iter__()
for num in it:
    print(num)
    break

print("=======")

for num in it:
    print(num)

# while True:
#     actual_iter = it.__iter__()
#     try:
#         elem = next(actual_iter)
#         print(elem)
#     except StopIteration:
#         break