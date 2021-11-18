from insert import Insert
from multiprocessing import Process

print("---Inserting image file into foto_pelanggan table---")
insert = Insert()
insert.iterating("source_images")
print(insert.countFiles("source_images"))