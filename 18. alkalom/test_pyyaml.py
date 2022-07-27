import yaml


my_dict = {"key": {
    "val1": ['alma', "körte"],
    "val2": None, 
    "val3": {
        "val4": [None]
    }
}}

with open("test.yaml", "w", encoding="utf-8") as f:
    yaml.dump(my_dict, f)


file_path = r"C:\WORK\2022_majus_prooktatas\18. alkalom\cars.yaml"

for data in yaml.safe_load_all(open(file_path)):
    print(data)
