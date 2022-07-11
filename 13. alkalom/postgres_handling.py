# 1. szükségünk  van 1 connection-re
############### 2. a connectinből létrehozunk egy database objectet
# 2. connection objectből példányosítunk egy cursor objectet - session


import psycopg2 as sql

connection = sql.connect(user="postgres",
                        password="postgres",
                        database="postgres",
                        host="localhost",
                        port=5432                     
                        )

cur = connection.cursor()

# első paraméter az sql script - kötelező

# kérjük le az aktuális időt
cur.execute("select now(), now(), 12, 'Ricsi'")
cur.execute("select * from cars")

# print(cur.fetchone())
# print(cur.fetchmany(2))
# print(cur.fetchall())

#######insert utasítás

#cur.execute("insert into brand (id, brand_name) values (1, 'Apple')")

# binding - data binding - bind változó
#cur.execute("insert into brand (id, brand_name) values (%s, %s)", (2, "Google"))

sql_script = "insert into brand (id, brand_name) values ({0}, '{1}')"

#cur.execute(sql_script.format(*(3, "Microsoft")))

cur.executemany("insert into brand (id, brand_name) values (%s, %s)", [(4, 'Huawei'),(5, 'Samsung')])


connection.commit()

connection.close()