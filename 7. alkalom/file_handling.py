# file műveletek

# 1. lépés: meg kell nyitni / létre kell hozni a filet
# 2. lépés: vagy adatot írunk a file-ba, vagy adatot kiolvasunk belőle
# 3. lépés: lezárjuk a file objektumot

# file felolvasása



file_path = r"C:\WORK\2022_majus_prooktatas\7. alkalom\Dracula.txt"

f = open(file_path, 'r', encoding="utf-8")
# my_data = f.read()
# my_data = f.readline()
my_data = f.readlines()

# if 'Dracula' in my_data:
#     print('megvan')

# for item in my_data:
#     if 'Dracula' in item:
#         print(item)

#print(my_data)

f.close()

# sortörés: \n


## file kiírás

f = open('test.txt', 'w', encoding="utf-8")

my_string = "ez egy string \n ez a szöveg új sorban lesz \n ez megint\n" * 100

#f.write(my_string)

f.writelines(my_data)

f.close()

