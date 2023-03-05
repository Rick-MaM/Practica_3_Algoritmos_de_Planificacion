import time 
from tkinter import *

class planning:

    def __init__(self):
        self.File()

    def File(self):
        with open("procesos.txt","r") as self.file:
            self.file = self.file.readlines()
    
    def FIFO(self):
        while len(self.file) != 0:
            process = self.file[0].split(",")
            print("Proceso: ", process[0], "------> ",end="")
            for count in range(int(process[2])):
                print(".", end="")
                time.sleep(1)
            print("Completado")
            self.file.pop(0)

proceso = planning()
proceso.FIFO()