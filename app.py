import glob
import os
import shutil

path = "C:\\2019\\*\\*SQLITE"


def getListOfFolder(path):
    list_of_folder = glob.glob(path)
    return list_of_folder


def checkIfDirectory(list_of_elements_in_path):
    list_of_directories = []
    for element in list_of_elements_in_path:
        if os.path.isdir(element):
            list_of_directories.append(element)
    return list_of_directories


def changeFolderName(list_of_directories_in_path):
    changed_folders = []
    for directory in list_of_directories_in_path:
        temp_dir = directory + '_temp'
        os.rename(directory, temp_dir)
        changed_folders.append(temp_dir)
    return changed_folders


def moveFiles(directories):
    numbers_of_sessions = 0
    for directory in directories:
        destination = "C:\\2019\\" + directory.split('\\')[2]
        for r, d, f in os.walk(directory):
            for file in f:
                print(f'Moving... \n {os.path.join(r, file)} to {os.path.join(destination, file)}')
                print(os.path.join(r, file))
                print(destination)
                shutil.move(r + '\\' + file, destination)
        numbers_of_sessions += 1
    print("{} sessions have been moved".format(numbers_of_sessions))


def deleteFolders(changed_folder_names):
    for folder in changed_folder_names:
        os.rmdir(folder)
        print(f"{folder} has been deleted")
    print(f'{len(changed_folder_names)} has been deleted ')


def main():

    list_of_elements_in_path = getListOfFolder(path)
    list_of_directories_in_path = checkIfDirectory(list_of_elements_in_path)
    changed_folder_names = changeFolderName(list_of_directories_in_path)
    print('')
    print(f'Folders after changed name:\n {changed_folder_names}')
    moveFiles(changed_folder_names)

    deleteFolders(changed_folder_names)


if __name__ == '__main__':
    main()
