###
# Creates a shopping list based on product names
# entered from the keyboard.
###

# Shopping list file name
shopping_list = 'shopping_list.txt'

# Adds a product name to the end of a shopping list
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')  

# Takes product names from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == "0":
        break  
    else:
        add_product(shopping_list, product)  
