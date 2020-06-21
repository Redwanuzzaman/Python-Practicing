import os
import shutil

print(os.getcwd())
original_path = "C:/Users/Md Redwanuzzaman/Desktop"
os.chdir(original_path)

print(os.getcwd())
try:
    os.makedirs('PyFolder')
except:
    print("Folder Already Exist")

with open(original_path + "/file 1.txt", "w+") as file1:
    pass

shutil.move(os.path.join(original_path, "file 1.txt"), os.path.join(original_path, "PyFolder"))
shutil.move(os.path.join(original_path, "file 1.txt"), os.path.join(original_path, "PyFolder"))
