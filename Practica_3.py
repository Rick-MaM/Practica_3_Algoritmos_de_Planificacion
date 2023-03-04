import time 
from tkinter import *

class planning:

    def __init__(self,windows):
        self.Windows = windows
        self.Windows.title("Algoritmo de Planificacion")
        self.Windows.geometry("400x400")
        self.File()

    def File(self):
        with open("procesos.txt","r") as self.file:
            self.file = self.file.readlines()

    
if __name__=="__main__":
    root=Tk()
    aplicacion = planning(root)
    root.mainloop()
