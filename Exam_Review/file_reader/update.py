import os

FILENAME = 'names.txt'
TEMP_FILE = 'temp'
READ_MODE = 'r'
WRITE_MODE = 'w'

source_file = open(FILENAME, READ_MODE)
temp_file = open(TEMP_FILE, WRITE_MODE)
with source_file, temp_file:
    for line in source_file:
        name, score = line.split()
        
        if name == 'Bob':
            score = 90
        
        if name == 'Cindy':
            name = 'Cynthia'
        
        temp_file.write(f'{name} {score}\n')

os.remove(FILENAME)
os.rename(TEMP_FILE, FILENAME)