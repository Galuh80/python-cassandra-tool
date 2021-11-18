from insert import Insert
import threading

print("---Inserting image file into foto_pelanggan table---")
insert = Insert()
image_threading = threading.Thread(insert.iterating("source_images"))
print(insert.countFiles("source_images"))

image_threading.start()
image_threading.join()
