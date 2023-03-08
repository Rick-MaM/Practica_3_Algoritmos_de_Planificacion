import time 
from tkinter import *

class Process:
    def __init__(self):
        self.File()

    def File(self):
        with open("procesos.txt","r") as self.file:
            self.file = self.file.readlines()
    
    def Round_Robin(self):
        quantum = 3
        file = self.file
        while len(file) != 0:
            process = file[0].split(",")
            time_process = int(process[2])
            print("Proceso: ", process[0], "----- ->",end="")
            for count_time in range(quantum):
                if time_process == 0:
                    break
                else:
                    time_process -= 1
                time.sleep(1)
                print(".",end="")
            if time_process > 0:
                print("Proceso: ", process[0], "------> ",time_process)
                file.append(process[0]+", "+process[1]+", "+str(time_process))
            else:
                print("Completado")
            file.pop(0)

    def shoter_time(self,list_SJF):
        Time = []
        for count_time in range(len(list_SJF)):
            process = list_SJF[count_time].split(",")
            Time.append(int(process[2]))
        Time.sort()
        return Time

    def SJF(self):
        aux_file = self.file
        times = self.shoter_time(aux_file)
        number_process = len(aux_file)
        while len(aux_file) != 0:
            for count_process in range(number_process+1):
                process = aux_file[count_process].split(",")
                if times[0] == int(process[2]):
                    print("Proceso: ",process[0], "------> ",end="")
                    for count in range(times[0]):
                        time.sleep(1)
                        print(".",end="")
                    print("completado")
                    break
            aux_file.pop(count_process)
            number_process = len(aux_file)
            times.pop(0)
  
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
    
    def process_priority(self,list_priority):
        number_priority = []
        for count_time in range(len(list_priority)):
            process = list_priority[count_time].split(",")
            number_priority.append(int(process[1]))
        number_priority.sort()
        return number_priority
    
    def priority(self):
        aux_file = self.file
        list_priority = self.process_priority(aux_file)
        number_process = len(aux_file)
        while len(aux_file) != 0:
            for count_process in range(number_process+1):
                process = aux_file[count_process].split(",")
                if list_priority[0] == int(process[1]):
                    print("Proceso: ", process[0], "------> ", end="")
                    for count in range(int(process[2])):
                        time.sleep(1)
                        print(".", end="")
                    print("completado")
                    break
            aux_file.pop(count_process)
            number_process = len(aux_file)
            list_priority.pop(0)

proceso = Process()
"""
print("-----> Round Robin <-----")
proceso.Round_Robin()
print("-----> SJF <-----")
proceso.SJF()
print("-----> FIFO <-----")
proceso.FIFO()
"""
print("-----> Prioridad <-----")
proceso.priority()
