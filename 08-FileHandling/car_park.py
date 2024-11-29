###
# Reads the entire contents of a file
###
def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

# Reads the entire file and splits lines into an array
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# Calculates the total number of cars parked
total = 0
for line in file_lines: 
    total += int(line) 

print('Total cars parked:', total) 
