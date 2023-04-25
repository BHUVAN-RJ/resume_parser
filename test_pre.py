



import os


folder = os.listdir('/Users/rjb/PycharmProjects/mllab/resume_parser/resume')
print(folder)

for item in folder:
    folder_path = "/Users/rjb/PycharmProjects/mllab/resume_parser/resume"
    print(item)
    new_name = item.replace(" ","")
    new_path = f"{folder_path}/{new_name}"
    old_path = f"{folder_path}/{item}"
    os.rename(old_path, new_path)
