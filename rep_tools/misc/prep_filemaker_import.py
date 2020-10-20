from FileFixer.locate_files import LocateFiles
from FileFixer.copy_rename import CopyRenameFile
from FileFixer.clear_folders import CleanFolder


def main():
    file_path_building_n_grounds = r"\\Cifs2\mmcondat$\Peoplesoft HR\B&G\*.*"
    loc_1 = LocateFiles(file_path_building_n_grounds)
    loc_1_latest_file = loc_1.locate_newest_file()

    file_1_dst = r"C:\Users\jt883\Desktop\Dest"
    file_1_rename = r"C:\Users\jt883\Desktop\Dest\TEST.csv"
    file_1 = CopyRenameFile(loc_1_latest_file, file_1_dst, file_1_rename)
    file_1.copy_and_rename_file()

    folder_1_path = r"C:\Users\jt883\Desktop\Clean"
    folder_1 = CleanFolder(folder_1_path)
    folder_1.clear_bygone_files()


if __name__ == '__main__':
    main()
