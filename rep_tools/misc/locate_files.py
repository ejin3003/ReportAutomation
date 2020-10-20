import os
import glob


class LocateFiles:
    # Functions within this class identifies the most recent file within a
    # specific filepath and returns its destination.
    def __init__(self, path):
        r"""
        path = r"filepath\*.*"
        Example Path: (r"C:\Users\name\Desktop\folder\*.*")
        """
        self.path = path

    def locate_newest_file(self):
        file_location = ''.join(self.path)
        newest_file_path = max(glob.glob(file_location), key=os.path.getmtime)
        # newest_file_name = os.path.basename(newest_file_path)
        return newest_file_path


# file_path = r"\\Cifs2\mmcondat$\Peoplesoft HR\B&G\*.*"
# location_1 = LocateFiles(file_path)
# location_1.locate_newest_file()



# file_dest = r"C:\Users\jt883\Desktop\Dest Test"
