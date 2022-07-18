book_stat_insert = """
insert into book_stat (book_name,
					   words_cnt,
					   rows_cnt,
					   page_cnt,
					   author,
					   release_date) values
(%s, %s, %s, %s, %s, %s)
returning id
"""

most_common_words_insert = """
insert into most_common_words (book_stat_id,
							   word_name,
							   word_cnt) values
(%s, %s, %s)
"""

db_params = {
    "user": "postgres",
    "password": "postgres",
    "db": "postgres",
    "host": "localhost",
    "port": 5432,
}


most_stats_insert = """
insert into most_stats (min_book,
						max_book) values
(%s, %s)

"""

select_book_id = """
select id from book_stat where book_name = '{book_name}'
"""