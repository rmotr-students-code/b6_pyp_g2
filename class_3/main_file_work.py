try:
    f = open('names.txt', 'r')
    for line in f:
        print(line + 20)
except:
    pass
finally:
    print("Closing the file!")
    f.close()


with open('names.txt', 'r') as f:
    for line in f:
        print(line + 20)


with People.all() as peps_it:
    for person in peps_it:
        print(person.name)
