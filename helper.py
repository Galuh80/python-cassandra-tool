import os, time

class Helper():

    def __init__(self):
        return self
    
    def setFolder(self, folderName):
        return os.getcwd() + "/" + folderName
    
    def convertToBinary(self, fileName):
        with open(fileName, "rb") as file:
            data = file.read()
        return data
    
    def countFiles(self, folderName):
        target = self.setFolder(folderName)
        return len(os.listdir(target))
    
    def iterateFiles(self, folderName):
        target = self.setFolder(folderName)

        start = time.time()
        
        for filename in os.listdir(target):
            file = os.path.join(target, filename)
            if os.path.isfile(file):
                print(filename)
        
        print(f'Required time : {time.time() - start} seconds')