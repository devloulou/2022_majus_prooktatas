folder_path = r"C:\WORK\2022_majus_prooktatas\14. alkalom\4_jsons"

cars_json_insert = """
insert into cars_json (id,
                        name,
                        miles_per_gallon,
                        cylinders,
                        displacement,
                        horsepower,
                        weight_in_lbs,
                        acceleration,
                        year,
                        origin) values
(nextval('seq_cars_json_id'), %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

db_params = {
    "user": "postgres",
    "password": "postgres",
    "db": "postgres",
    "host": "localhost",
    "port": 5432,
}