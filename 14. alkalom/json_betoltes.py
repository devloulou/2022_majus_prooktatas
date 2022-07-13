# ezeket a json-ket be fogjuk tölteni adatbázisba
# létre kell hoznunk 1 táblát
# meg kell írnunk a betöltőt
# SQL feladatok


"""
BI Fejlesztő - Business Intelligence fejlesztő
Data Engineer

ETL - Extract Transform Load - backend rétegen történik a transform -> python a backend
ELT - Extract Load Transform - a backend "csak" közvetítő szerepet vállal


"""
import os


from utils.db_handler import run_sql
from utils.file_handler import get_file_list, get_data_from_json
from utils.params import folder_path, cars_json_insert, db_params


def etl():    
    for item in get_file_list(folder_path):
        json_path = os.path.join(folder_path, item)
        data = get_data_from_json(json_path)
        
        run_sql(db_params, cars_json_insert, tuple(data.values()))        

if __name__ == '__main__':
    etl()