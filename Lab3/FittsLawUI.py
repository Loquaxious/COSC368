from tkinter import *
from tkinter.ttk import * 
import random
import csv
import time

class FittsLawUI:
    def __init__(self, window):
        self.window = window
        self.distances = [64, 128, 256, 512]
        self.widths = [8, 16, 32]
        self.combo = []
        self.name = 'Logan'
        self.file = open('FittsLawLog.xlsx', 'w', newline='')
        self.writer = csv.writer(self.file)        
        self.i = 0
        self.count = 0
        self.fc = True
        self.main = Canvas(window, width=600, height = 600)
        self.main.pack()
        self.make_combo()
        self.build_experiment()
    
    def build_experiment(self):
        width, dist = self.combo[0]
        tspan = dist + width
        margin = (600 - tspan) / 2        
        self.left = self.main.create_rectangle(margin, 0, margin + width, 600, fill='blue')
        self.right = self.main.create_rectangle(margin + dist, 0, margin + width + dist, 600, fill='green', tag='target')
        self.main.tag_bind('target', "<ButtonPress-1>", self.clicked)
        
    def clicked(self, event):
        if self.fc:
            self.time = time.time()
            self.fc = False
        else:
            if self.i == 12:
                self.experiment_over()
            else:
                self.write_log()
        
        self.main.dtag(CURRENT, 'target')
        
        self.count += 1      
        
        if self.count == 4:
            self.i += 1
            self.count = 0
            if self.i == 12:
                self.experiment_over()
            else:
                self.update_rectangles()          
        
        if self.count % 2 == 0:
            self.main.itemconfigure(self.left, fill='blue')
            self.main.itemconfigure(self.right, fill='green', tag='target')            
        else:
            self.main.itemconfigure(self.left, fill='green', tag='target')
            self.main.itemconfigure(self.right, fill='blue')
            
        print('i: ', self.i)
        print('count: ', self.count)
        
    def write_log(self):
        total_time = (time.time() - self.time)
        self.writer.writerow([self.name, self.combo[self.i][1], \
                              self.combo[self.i][0], self.count + 1, total_time])
        self.time = time.time()
        
    def update_rectangles(self):
        tspan = self.combo[self.i][0] + self.combo[self.i][1]
        margin = (600 - tspan) / 2         
        self.main.coords(self.left, margin, 0, margin + self.combo[self.i][0], 600)
        self.main.coords(self.right, margin + self.combo[self.i][1], 0, margin +  \
                         self.combo[self.i][0] + self.combo[self.i][1], 600)
        
    def make_combo(self):
        for dist in self.distances:
            for width in self.widths:
                self.combo.append((width, dist))
        random.shuffle(self.combo)
        
    def experiment_over(self):
        self.main.tag_unbind('target', "<ButtonPress-1>")
        self.main.itemconfigure(self.left, fill='blue')
        self.main.itemconfigure(self.right, fill='blue')        
        self.file.close()
        
def main():
    window = Tk()
    experiment = FittsLawUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()