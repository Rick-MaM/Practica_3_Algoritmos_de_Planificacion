import time 
from tkinter import *

class Process:
    def __init__(self):
        self.File()

    def File(self):
        with open("procesos.txt","r") as self.file:
            self.file = self.file.readlines()

    def SJF(self):
        for count_process in range (len(self.file)):
            for count_time in range (len(self.file)):
                process = self.file[count_time].split(",")
                if int(process[2]) == count_process:
                    time.sleep(int(process[2]))
                    print("Proceso: ", process[0],
                          "------> Completado", "------> Tiempo: ",int(process[2]))
            
    def FIFO(self):
        aux_file = self.file
        while len(aux_file) != 0:
            process = aux_file[0].split(",")
            print("Proceso: ", process[0], "------> ",end="")
            for count in range(int(process[2])):
                print(".", end="")
                time.sleep(1)
            print("Completado")
            aux_file.pop(0)
    
    def process_priority(self):
        last_process = 0
        for count_limit in range(len(self.file)):
            process = self.file[count_limit].split(",")
            if int(process[1]) > last_process:
                last_process = int(process[1])
        return last_process
    
    def Priority(self):
        count_process = 0
        while count_process <= self.process_priority():
            for count in range(len(self.file)):
                process = self.file[count].split(",")
                if int(process[1]) == count_process:
                    time.sleep(int(process[2]))
                    print("Proceso: ", process[0], "------> Completado")
            count_process += 1

proceso = Process()
proceso.SJF()
