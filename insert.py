from helper import Helper
from connector import Connector
import uuid, time, os

class Insert(Helper):

    def __init__(self):
        pass

    def insertImage(self, filename, img):
        conn = Connector.createConnection()
        if conn is not None:
            conn.execute("""INSERT INTO foto_pelanggan(id, file_foto, nama_file) VALUES (%(id)s, %(file_foto)s, %(nama_file)s) """, {'id':uuid.uuid1(), 'file_foto':img, 'nama_file':filename})
        else:
            print("Failed insert images")

    def iterating(self, folder):
        target = self.setFolder(folder)

        start = time.time()

        for filename in os.listdir(target):
            file = os.path.join(target, filename)
            if os.path.isfile(file):
                print(file)
                img = self.convertToBinary(file)
                self.insertImage(filename, img)
        
        print(f'Required time : {time.time() - start} seconds')
