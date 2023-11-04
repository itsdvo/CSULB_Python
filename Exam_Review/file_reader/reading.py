FILENAME = 'names.txt'
READ_MODE = 'r'

with open(FILENAME, READ_MODE) as names_file:
    for line in names_file:
        name, score = line.split()
        print(f'Name: {name}, Score: {score}')