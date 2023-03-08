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
        self.File()
        while len(self.file) != 0:
            process = self.file[0].split(",")
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
                self.file.append(process[0]+", "+process[1]+", "+str(time_process))
            else:
                print("Completado")
            self.file.pop(0)

    def shoter_time(self,list_SJF):
        Time = []
        for count_time in range(len(list_SJF)):
            process = list_SJF[count_time].split(",")
            Time.append(int(process[2]))
        Time.sort()
        return Time

    def SJF(self):
        self.File()
        times = self.shoter_time(self.file)
        number_process = len(self.file)
        while len(self.file) != 0:
            for count_process in range(number_process+1):
                process = self.file[count_process].split(",")
                if times[0] == int(process[2]):
                    print("Proceso: ",process[0], "------> ",end="")
                    for count in range(times[0]):
                        time.sleep(1)
                        print(".",end="")
                    print("completado")
                    break
            self.file.pop(count_process)
            number_process = len(self.file)
            times.pop(0)
  
    def FIFO(self):
        self.Fiel()
        while len(self.file) != 0:
            process = self.file[0].split(",")
            print("Proceso: ", process[0], "------> ",end="")
            for count in range(int(process[2])):
                print(".", end="")
                time.sleep(1)
            print("Completado")
            self.file.pop(0)
    
    def process_priority(self,list_priority):
        number_priority = []
        for count_time in range(len(list_priority)):
            process = list_priority[count_time].split(",")
            number_priority.append(int(process[1]))
        number_priority.sort()
        return number_priority
    
    def priority(self):
        self.File()
        list_priority = self.process_priority(self.file)
        number_process = len(self.file)
        while len(self.file) != 0:
            for count_process in range(number_process+1):
                process = self.file[count_process].split(",")
                if list_priority[0] == int(process[1]):
                    print("Proceso: ", process[0], "------> ", end="")
                    for count in range(int(process[2])):
                        time.sleep(1)
                        print(".", end="")
                    print("completado")
                    break
            self.file.pop(count_process)
            number_process = len(self.file)
            list_priority.pop(0)

proceso = Process()

print("-----> Round Robin <-----")
proceso.Round_Robin()
print("-----> SJF <-----")
proceso.SJF()
print("-----> FIFO <-----")
proceso.FIFO()
print("-----> Prioridad <-----")
proceso.priority()
