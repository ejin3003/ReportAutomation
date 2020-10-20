import os
import glob
import datetime as dt

print('Import MGHCart.csv')

# Sets the desired directory and saves the path of the most recent file within said directory
file_location = r"E:\Data\Documents\PSOFT\JB_CART_ITEMS_ALL_PHS_CARTS\*.*"
recent_import = max(glob.glob(file_location), key=os.path.getmtime)
copy_destination = recent_import.replace(r'PSOFT\JB_CART_ITEMS_ALL_PHS_CARTS', r'FM Import\Turns Report')
print(recent_import)
print(copy_destination)

# Removes digits from the designated file path
output = ""
for char in copy_destination:
    if char == ".":
        output += 'MGHCart' + '.'
    elif not char.isdigit():
        output += char

output = output.replace('JB_CART_ITEMS_MGH-', '')
print(output)

print('*************************')

print('Import MGH90.csv')

# Sets the desired directory and saves the path of the most recent file within said directory
file_location_2 = r"E:\Data\Documents\PSOFT\PHSIN142_Department_Usage_Summary_90_Days_PHS\*.*"
recent_import_2 = max(glob.glob(file_location_2), key=os.path.getmtime)
copy_destination_2 = recent_import_2.replace(r'PSOFT\PHSIN142_Department_Usage_Summary_90_Days_PHS', r'FM Import\Turns Report')
print(recent_import_2)
print(copy_destination_2)


# Removes digits from the designated file path
output_2 = ""
for char in copy_destination_2:
    if char == ".":
        output_2 += 'MGH90' + '.'
    elif not char.isdigit():
        output_2 += char
output_2 = output_2.replace('JB_PHSIN-', '')
print(output_2)

print('*************************')
