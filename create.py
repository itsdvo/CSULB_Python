FILENAME = 'names.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as names_file:
    names_file.write('Alice 97\n')
    names_file.write('Bob 35\n')
    names_file.write('Cindy 95\n')