import os
import time
import glob

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), r'OneDrive\Desktop')
src_file = r"{}".format(desktop) + r"\shipping_tables.xlsx"

# created_date_time = os.path.getctime(src_file) - 1 * 86400
# print(time.ctime(created_date_time))

# Prints the filepath of the most recent file within the designated folder
file_loc = r"C:\Users\ejin3\OneDrive\Desktop\Python\Refrence Material\*.*"
recent_file = max(glob.glob(file_loc), key=os.path.getmtime)
print(recent_file)
