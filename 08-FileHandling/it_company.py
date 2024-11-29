###
# Saves to a file a list of employees working at a specified position.
###

# File names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# Write selected employees to a file
with open(employees_file, 'r') as file:  
    with open(position_file, 'w') as output_file:  
        for line in file:
            if job_title in line:  
                output_file.write(line)  
