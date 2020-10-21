import os, time, sys
import glob
import datetime as dt
from shutil import copyfile

####### Import MGHCart.csv ######

# Sets the desired directory and saves the path of the most recent file within said directory
file_location = r"E:\Data\Documents\PSOFT\JB_CART_ITEMS_ALL_PHS_CARTS\*.*"
recent_import = max(glob.glob(file_location), key=os.path.getmtime)
copy_destination = recent_import.replace(r'PSOFT\JB_CART_ITEMS_ALL_PHS_CARTS', r'FM Import\Turns Report')

# Removes digits from the designated file path
output = ""
for char in copy_destination:
    if char == ".":
        output += 'MGHCart' + '.'
    elif not char.isdigit():
        output += char
output = output.replace('JB_CART_ITEMS_MGH-', '')

copyfile(recent_import, copy_destination)

if os.path.exists(output):
    os.remove(output)

# Renames the designated file
src = copy_destination
dst = output
os.rename(src, dst)

########################

###### Import MGH90.csv ######
# Sets the desired directory and saves the path of the most recent file within said directory
file_location_2 = r"E:\Data\Documents\PSOFT\PHSIN142_Department_Usage_Summary_90_Days_PHS\*.*"
recent_import_2 = max(glob.glob(file_location_2), key=os.path.getmtime)
copy_destination_2 = recent_import_2.replace(r'PSOFT\PHSIN142_Department_Usage_Summary_90_Days_PHS', r'FM Import\Turns Report')

# Removes digits from the designated file path
output_2 = ""
for char in copy_destination_2:
    if char == ".":
        output_2 += 'MGH90' + '.'
    elif not char.isdigit():
        output_2 += char
output_2 = output_2.replace('JB_PHSIN-', '')

copyfile(recent_import_2, copy_destination_2)

if os.path.exists(output_2):
    os.remove(output_2)

# Renames the designated file
src_2 = copy_destination_2
dst_2 = output_2
os.rename(src_2, dst_2)

########################

# Removes Files Older than Seven Days
path_mgh_cart = r"E:\Data\Documents\PSOFT\JB_CART_ITEMS_ALL_PHS_CARTS"
path_mgh_90 = r"E:\Data\Documents\PSOFT\PHSIN142_Department_Usage_Summary_90_Days_PHS"
now = time.time()

# MGHCart
for file in os.listdir(path_mgh_cart):
    if os.path.getmtime(os.path.join(path_mgh_cart, file)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path_mgh_cart, file)):
            os.remove(os.path.join(path_mgh_cart, file))

# MGH90
for file_2 in os.listdir(path_mgh_90):
    if os.path.getmtime(os.path.join(path_mgh_90, file_2)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path_mgh_90, file_2)):
            os.remove(os.path.join(path_mgh_90, file_2))
