

import os


print(f"Current working directory: {os.getcwd()}")

my_path = "C:/CNET332_S2"
if not os.path.exists(my_path):
    print('\t'f"making a new directory: {my_path}")
    os.mkdir(my_path)

os.chdir(my_path)
print('\t'f"changing the current working directory as: {os.getcwd()}")

print(f"Current working directory: {os.getcwd()}")

login = os.getlogin()
print(f"Login details: {login}")

work_path = "work_4"
sub_path = os.path.join(my_path, work_path)
if not os.path.exists(sub_path):
    print('\t'f"making a new directory: {sub_path}")
    os.mkdir(sub_path)

firstName = "XXXX"
lastName = "XXXXXX"
firstName_path = os.path.join(sub_path, firstName)
lastName_path = os.path.join(firstName_path, lastName)
print('\t'f"making new directories with first name and last name: {firstName_path}/{lastName}")
if not os.path.exists(lastName_path):
    os.makedirs(lastName_path)

osName = os.name
print(f"OS name: {osName}")

otherPath = os.path.join(sub_path, "l", "m", "n")
print('\t'f"making new directories: {otherPath}")
if not os.path.exists(otherPath):
    os.makedirs(otherPath)

studentNumber = "XXXXXX"
studentNumber_path = os.path.join(sub_path, studentNumber)
print('\t'f"making a new directory: {studentNumber_path}")
if not os.path.exists(studentNumber_path):
    os.mkdir(studentNumber_path)

work_4_lists = os.listdir(sub_path)
print(f"Listing directories: {work_4_lists}")

print(f"Doing a walk: {my_path}")
for root, dirs, files in os.walk(my_path):
    root = root.replace("\\", "\\\\")
    print('\t' + f"{root}, {dirs}, {files}")

print('\t'f"removing the directory with the student number")
if os.path.exists(studentNumber_path):
    os.rmdir(studentNumber_path)

print(f"Doing a walk: {my_path}")
print(f"Removing the directory with the student number")
for root, dirs, files in os.walk(my_path):
    print('\t' + f"{root}, {dirs}, {files}")
