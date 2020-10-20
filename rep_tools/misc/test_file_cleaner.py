import os, time, sys
import glob
import datetime as dt

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
                          
