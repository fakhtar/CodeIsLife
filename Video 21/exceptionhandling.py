try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print(e)
    print('This is where other code would go if the file does not exist.')
else:
    print(f.read())
    f.close()

