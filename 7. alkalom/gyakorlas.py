# leghosszab sor
# állpítsuk meg, hogy hány oldalas a könyv: 3000 karakter 1 oldal
# legrövidebb sor: üres sor az nem számít
# leggyakrabban elóforduló 5 szó

# prototipizálás
"""
1. lépés: a file-t fel kell olvasnom és szükségem van az adatára
2. statisztikák előállítása
    a, hány oldalas a könyv
    b, legrövidebb és leghosszabb sor
    c, leggyakrabban előforduló 5 szó
"""
# hülye biztos: edge case illetve corner case
import os
import math


def get_data_from_txt(file_path):
    if not os.path.exists(file_path):
        raise Exception(f"Nem létezik az elérési útvonal: {file_path}")
        return False, f"Nem létezik az elérési útvonal: {file_path}"
    with open(file_path, "r", encoding="utf-8") as f:
        my_data = f.read()
    return my_data
    

def create_statistics(data):
    page_num = math.ceil(len(data)/3000)
    temp_data = [item for item in data.split("\n")]

    min_row = len(temp_data[0])
    max_row = 0
    my_stat = {}
    for idx, item in enumerate(temp_data):
        if min_row > len(item) and len(item) != 0:
            my_stat['min_row'] = {"row": idx + 1, "value": len(item)}
            min_row = len(item) 
        if len(item) > max_row:
            my_stat['max_row'] = {"row": idx + 1, "value": len(item)}
            max_row = len(item)

    print(my_stat)

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), 'Dracula.txt')
    data = get_data_from_txt(file_path)

    create_statistics(data)