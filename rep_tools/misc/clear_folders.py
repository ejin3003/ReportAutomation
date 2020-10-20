import os
import time


class CleanFolder:
    def __init__(self, path):
        self.path = path

    def clear_bygone_files(self):
        now = time.time()
        for file in os.listdir(self.path):
            if os.path.getmtime(os.path.join(self.path, file)) < now - 7 * 86400:
                if os.path.isfile(os.path.join(self.path, file)):
                    print(file)
                    print(os.path.getmtime(os.path.join(self.path, file)))
                    os.remove((os.path.join(self.path, file)))


# folder_path = r"C:\Users\jt883\Desktop\Clean"
# folder_1 = CleanFolder(folder_path)
# folder_1.clear_bygone_files()
