try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print(e)
    print('This is where other code would go if the does not exist.')
else:
    print(f.read())
    f.close()

