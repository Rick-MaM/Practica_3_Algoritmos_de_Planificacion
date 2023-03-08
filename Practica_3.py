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
            for count_time in range(quantum):
                if time_process == 0:
                    break
                else:
                    time_process -= 1
                time.sleep(1)
            if time_process > 0:
                print("Proceso: ", process[0], "------> ",time_process)
                file.append(process[0]+", "+process[1]+", "+str(time_process))
            else:
                print("Proceso: ", process[0], "------> Completado")
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