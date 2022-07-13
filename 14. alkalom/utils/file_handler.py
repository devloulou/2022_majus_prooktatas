"""
1. kell egy lista a file-okról
2. meg kell tudnom nyitni a json-ket és kiolvasni belőle az adatot

"""
import os
import json

def get_file_list(path):
    if not os.path.exists(path):
        raise FileExistsError(f"A megadott elérési útvonal nem található: {path}")
    
    return list(os.listdir(path))

def get_data_from_json(json_path):
    if not os.path.exists(json_path):
        raise FileExistsError(f"A megadott file nem található: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data

if __name__ == '__main__':
    from params import folder_path
    json_list = get_file_list(folder_path)

    json_path = os.path.join(folder_path, json_list[0])
    data = get_data_from_json(json_path)

    print(data)