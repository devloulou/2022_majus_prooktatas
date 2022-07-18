"""
1. kell egy connection object - ehhez egy függvényt fogunk csinálni
2. kell egy olyen függvény, ami megfuttatja nekünk az sql utasítást
3. kell egy insert scriptet írnunk
"""

import psycopg2 as sql


def get_connection(connection_params):
    return sql.connect(user=connection_params['user'],
                        password=connection_params['password'],
                        database=connection_params['db'],
                        host=connection_params['host'],
                        port=connection_params['port'])

def run_sql(connection_params, sql_script, data=None):
    with get_connection(connection_params) as conn:
        with conn.cursor() as cur:
            try:
                if data:
                    cur.execute(sql_script, data)
                    try:
                        book_stat_id = cur.fetchone()[0]
                    except:
                        book_stat_id = None
                else:
                    cur.execute(sql_script)
            except Exception as e:
                conn.rollback()
                print(e)

            conn.commit()

    return book_stat_id


def run_select(connection_params, sql_script):
    with get_connection(connection_params) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(sql_script)
            except Exception as e:
                print(e)

            data = cur.fetchall()

    return data



if __name__ == '__main__':
    from params import book_stat_insert, db_params, most_common_words_insert

    data = run_select(db_params, 'select now()')

    print(data)
    # id = run_sql(db_params, book_stat_insert, ('Harry Potter', 100, 10, 10, 'J.K. Rowling', 'september, 2000'))

    # run_sql(db_params, most_common_words_insert, (id, 'and', '2000'))