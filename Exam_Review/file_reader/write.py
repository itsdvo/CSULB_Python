## different ways to write

FILENAME = 'names.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Jack 87\n')

    # demo of writing variable data
    name = 'Chad'
    score = 69
    names_file.write(f'{name} {score}\n')

    names_file.write('Amy 65\n')