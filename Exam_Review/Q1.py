# Define the constant for number of rows
ROWS = 26

# Loop through each row
for i in range(1, ROWS + 1):
    # Use the chr function to get the character, starting from 97 (which is 'a')
    character = chr(96 + i)
    
    # Print the pattern for each row
    print(f"{i} {'*' * i}{character * i}")
