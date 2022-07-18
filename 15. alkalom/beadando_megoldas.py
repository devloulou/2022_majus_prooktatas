# felolvassuk a file-okat egy listába
# egyesével megnyitjuk ezeket a file-okat
# előllítjuk egyesével a statisztikákat
# 2. feladatban megadott statisztikák elkészítése
# ki írjuk a statisztikát
import os
import json
import math
from collections import Counter

from utils.params import (db_params,
                        most_common_words_insert,
                        book_stat_insert,
                        most_stats_insert,
                        select_book_id)
from utils.db_handler import run_sql, run_select

FOLDER_LOCATION = os.path.join(os.path.dirname(__file__), 'books')

def get_files():
    return [os.path.join(FOLDER_LOCATION, item) for item in os.listdir(FOLDER_LOCATION) if item.endswith('.txt')]

def get_data_from_txt(file_loc):
    if not os.path.exists(file_loc):
        raise FileExistsError('A megadott file nem található!')
    
    with open(file_loc, "r", encoding="utf-8") as f:
        data = f.read()

    return data

def write_json(file_loc, data):    
    if not os.path.exists(os.path.dirname(file_loc)):
        raise FileExistsError(f'A megadott elérési út található: {os.path.dirname(file_loc)}')
    
    with open(file_loc, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return True

def word_counter(data):
    return len([item for item in data.split(' ') if len(item) > 2])

def row_counter(data):
    return len(data.split('\n'))

def page_counter(data):
    return math.ceil(len(data)/3000)

def get_author(data):
    for row in data.split('\n'):
        if 'Author:' in row:
            return row[7:].strip()
            

def get_release_date(data):
    for row in data.split('\n'):
        if 'Release Date:' in row:
            return row.split(' [')[0][13:].strip()
        if 'Posting Date:' in row:
            return row.split(' [')[0][13:].strip()   

def get_most_common_words(data):
    c = Counter([item for item in data.split(' ') if len(item) > 2])
    return c.most_common(5)

def run():
    statistics = {}

    min_val = None
    max_val = None
    most_stats = {}
    for idx, item in enumerate(get_files()):
        data = get_data_from_txt(item)
        
        statistics['könyv_neve'] = item.split('\\')[-1][0:-4]
        statistics["szavak_száma"] = word_counter(data)
        statistics["sorok_száma"] = row_counter(data)
        statistics["oldalak_száma"] = page_counter(data)
        statistics["szerző"] = get_author(data)
        statistics["könyv_megjelenés"] = get_release_date(data)
        statistics["leggyakoribb"] = {item[0]:item[1] for item in get_most_common_words(data)}
        
        json_location = os.path.join(FOLDER_LOCATION, item.split('\\')[-1][0:-4] + '.json')
        # kell egy insert a book_stat táblába
        # kell egy insert a most_common_word táblába

        book_stat_id = run_sql(db_params, book_stat_insert, tuple(statistics.values())[0:-1])
        
        for k, v in statistics["leggyakoribb"].items():            
            run_sql(db_params, most_common_words_insert, (book_stat_id, k, v))            

        if idx == 0:
            min_val = statistics["oldalak_száma"]
            max_val = statistics["oldalak_száma"]
            most_stats['legrövidebb'] = item.split('\\')[-1][0:-4]
            most_stats['leghosszabb'] = item.split('\\')[-1][0:-4]


        if min_val > statistics["oldalak_száma"]:
            min_val = statistics["oldalak_száma"]
            most_stats['legrövidebb'] = item.split('\\')[-1][0:-4]
        
        if statistics["oldalak_száma"] > max_val:
            max_val = statistics["oldalak_száma"]
            most_stats['leghosszabb'] = item.split('\\')[-1][0:-4]


    #os.remove(os.path.join(FOLDER_LOCATION, most_stats['legrövidebb'] + '.txt'))
    #os.remove(os.path.join(FOLDER_LOCATION, most_stats['legrövidebb'] + '.json'))
    
    #most_stats['törölt_könyv'] = most_stats['legrövidebb']
    #print(most_stats)
    ids = []
    for k, v in most_stats.items():
        temp_id = run_select(db_params, select_book_id.format(book_name=v.replace('\'', '\'\'')))
        ids.append(temp_id[0][0])

    run_sql(db_params, most_stats_insert, tuple(ids))
    #write_json(os.path.join(os.path.dirname(__file__), 'statistics.json'), most_stats)

if __name__ == '__main__':
    run()