FILENAME = 'names.txt'
READ_MODE = 'r'

name = 'Taylor Swift'
signature = 0

for letter in name:
    signature += ord(letter)

with open(FILENAME, READ_MODE) as names_file:
    count = 0
    total = 0
    for line in names_file:
        name, score_str = line.split()
        try:
            score = float(score_str)
            count += 1
            total += 1
        except:
            pass
    print(f'average is {total/count}, Signature: {signature}')