import os 
import shutil 
import time 

from_dir = "C:/Users/Satyam/Downloads"
to_dir = "C:/Users/Satyam/Desktop"

list_of_files = os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    root,extension = os.path.splitext(file_name)
    print(root)
    print(extension)

    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document-files"
        path3 = to_dir + '/' + "Document-files" + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "....")
            shutil.move(path1,path3)
        else :  
            os.makedirs(path2)
            print("Moving" + file_name + "....")
            shutil.move(path1,path3)