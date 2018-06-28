import sys
import os
import time
#import C
#import Python
#import Cplus
#import Result
#import Plot

c1=0
c2=0
p=0


from tkinter import *

class Application(Frame):
    def executeC(self):
         print ("Run C")
         c1=1
         self.QUIT["command"] = self.quit
         
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "ALL"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "C"
        self.hi_there["command"] = self.executeC 

        self.hi_there.pack({"side": "left"})
        
        self.python = Button(self)
        self.python["text"] = "python",
        self.python["command"] = self.quit

        self.python.pack({"side": "left"})
        
        self.cpp = Button(self)
        self.cpp["text"] = "CPlus",
        self.cpp["command"] = self.quit

        self.cpp.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()





t1=time.time()

print("enter 1 or 0 for c , cplus, python \n")


print("\n.........................")
if c1==1:
    #executeC()
    cmd1='gcc clarge.c'
    os.system(cmd1)
    cmd2='.\a.out'
    os.system(cmd2)
    t2=time.time()-t1
    print(t2)
print("\n.........................")
if c2==1:
    #1Cplus.executeCplus()
    cmd1='g++ cpplarge.cpp'
    os.system(cmd1)
    cmd2='.\a.out'
    os.system(cmd2)
    t3=time.time()-t2
    print(t3)
print("\n.........................")
if p==1:
    #Python.executePython()
    cmd='python plarge.py'
    os.system(cmd)
    t4=time.time()-t3
    print(t4)
   # cmd='s'
    #os.system(cmd)
    
#Result.executionResult()
#import makeResult as m
#m.makecsv()

print("\n.........................")
#Plot.executePlot()    
# importing the required module
import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [t2,t3,t4]
 
# plotting the points 
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('file-size')
# naming the y axis
plt.ylabel('time-taken')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()    