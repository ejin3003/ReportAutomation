import os
from shutil import copy2


class CopyRenameFile:
    def __init__(self, path, dest, new_file_name):
        self.path = path,
        self.dest = dest,
        self.new_file_rename = new_file_name

    def copy_and_rename_file(self):
        file_destination = ''.join(self.dest)
        file_path = ''.join(self.path)
        renamed_file = ''.join(self.new_file_rename)
        if os.path.exists(renamed_file):
            os.remove(renamed_file)
        copy2(file_path, file_destination)
        newest_file_name = "\\" + os.path.basename(file_path)
        os.rename(file_destination + newest_file_name, renamed_file)


# files_path = r"C:\Users\jt883\Desktop\Path\May.xlsx"
# files_dest = r"C:\Users\jt883\Desktop\Dest"
# files_name = r"C:\Users\jt883\Desktop\Dest\April.xlsx"
#
# copy_1 = CopyRenameFile(files_path, files_dest, files_name)
# copy_1.copy_and_rename_file()
