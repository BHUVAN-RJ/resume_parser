import os


def preprocess(folder_original_path):
    folder = os.listdir(folder_original_path)
    for item in folder:
        folder_path = folder_original_path
        new_name = item.replace(" ","")
        new_path = f"{folder_path}/{new_name}"
        old_path = f"{folder_path}/{item}"
        os.rename(old_path, new_path)