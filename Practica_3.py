import time 

class planning:

    def __init__(self):
        pass

    def File(self):
        with open("procesos.txt","r") as file:
            file = file.readlines()
        return file
    
    
    

proceso = planning()
file = proceso.File()
print(file[1])