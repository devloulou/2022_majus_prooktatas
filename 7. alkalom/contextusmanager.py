# contextusmanager
# with 

file_path = "7. alkalom/Dracula.txt"
#file_path = r"C:\WORK\2022_majus_prooktatas\7. alkalom\motor_wltp.xlsx"

with open(file_path, "r", encoding="utf-8") as f:
    my_data = f.read()

print(my_data)