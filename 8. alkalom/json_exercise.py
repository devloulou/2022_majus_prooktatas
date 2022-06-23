# meg kellene vizsgálni ezeket a file-okat
# megnézni, hogy milyen kulcsaik vannak
# van e eltérés a kulcsok között

# legerősebb autó
# leggyengébb
# legöregebb
# legfiatalabb

# json-be írjuk ki a statisztikát
#########################################################
# szükségem van a file-okat listájára - Done
# meg kell nyitnom olvasásra a file-okat - Done
# meg kell vizsgálni a struktúrát

# le kell gyártani a statisztikát

import os
import json

# constans deklaráció
FOLDER_PATH = os.path.join(os.path.dirname(__file__), "4_jsons")
main_keys = []

def get_files_list():
    return [item for item in os.listdir(FOLDER_PATH) if item.endswith('.json')]

def read_data_from_json(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"A megadott file {file_path} nem létezik")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

# rekurzió
def examine_structure_test(file_obj: dict):
    for key, value in file_obj.items():
        if type(value) == list:
            for item in value:
                if type(item) == dict:
                    pass
                elif type(item) == list:
                    pass
                else:
                    pass
        elif type(value) == dict:
            for k, v in value.items():
                if type(v) == list:
                    pass
                elif type(v) == dict:
                    pass
                else:
                    pass
        else:
            pass


def examine_structure(file_obj: dict):
    keys = list(file_obj.keys())

    # main_minus_keys = []

    # for item in main_keys:
    #     if item not in keys:
    #         main_minus_keys.append(item)

    # keys_minus_main = []

    # for item in keys:
    #     if item not in main_keys:
    #         keys_minus_main.append(item)    
    
    main_minus_keys = set(main_keys).difference(set(keys))
    keys_minus_main = set(keys).difference(set(main_keys))

    if len(main_minus_keys) > 0:
        print(main_minus_keys)
    
    if len(keys_minus_main) > 0:
        print(keys_minus_main)


if __name__ == '__main__':
    main_keys = [key for key in read_data_from_json(r"C:\WORK\2022_majus_prooktatas\8. alkalom\4_jsons\1_car.json")]

    files_list = get_files_list()
    
    for item in files_list[0:]:

        json_path = os.path.join(FOLDER_PATH, item)
        data = read_data_from_json(json_path)
        examine_structure(data)