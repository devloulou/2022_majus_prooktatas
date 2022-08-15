import os
import math
import json
import time
from pymongo import MongoClient

db_uri = "mongodb://localhost:27017"

client = MongoClient(db_uri)
database = client['pelda']
coll = database['test_col']


def read_data(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


folder_location = r"C:\WORK\2022_majus_prooktatas\22. alkalom\4_jsons"
my_list =os.listdir(folder_location) 

list_len = len(my_list)
# print(list_len)

batch_size = 1200

iter_num = math.ceil(list_len / batch_size)


# start_time = time.time()
# for r in range(12):
#     cnt = 0
#     for i in range(iter_num):
#         data = []
#         if i == 0:
#             for f in my_list[0:batch_size]:
#                 temp = read_data(os.path.join(folder_location, f))
#                 data.append(temp)
#                 # coll.insert_one(temp)

#         elif i > 0 and (iter_num - 1 ) > i:
#             cnt += 1
#             for f in my_list[cnt*batch_size:cnt*batch_size+batch_size]:
#                 temp = read_data(os.path.join(folder_location, f))
#                 data.append(temp)
#                 # coll.insert_one(temp)
#         else:
#             for f in my_list[i*batch_size:]:
#                 temp = read_data(os.path.join(folder_location, f))
#                 data.append(temp)
#                 # coll.insert_one(temp)
#         coll.insert_many(data)

# end_time = time.time() - start_time

# print(end_time)

# lassú 0.2966794967651367

# gyors 0.06799697875976562

# start_time = time.time()
# for r in range(12):
#     for f in my_list:
#         temp = read_data(os.path.join(folder_location, f))
#         coll.insert_one(temp)

# end_time = time.time() - start_time
# print(end_time)

# 9800 - 1.135385513305664 - insert_many - bulk insert
# 6.003131151199341

query = {'Horsepower': {'$gt': 140}}

cnt = 0

temp = coll.find({})

import sys

print(sys.getsizeof(temp))

for item in temp.batch_size(300):
    cnt += 1
    print(sys.getsizeof(item))
    break
