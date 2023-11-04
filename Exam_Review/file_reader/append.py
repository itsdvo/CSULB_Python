# File name
FILENAME = 'names.txt'

# Open the file in append mode
with open(FILENAME, 'a') as file:
    # Example of new name and score to add
    new_name = 'John'
    new_score = '85'
    
    # Write the new entry to the file
    file.write(f'{new_name} {new_score}\n')

# Print out confirmation
print("New entry added to the file.")
