from tkinter import *
from tkinter.ttk import * 
import random
import time
import csv


class KeyboardGUI:
    def __init__(self, window):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.window = window
        self.generate_random_board()
        self.target_letters = self.letters[:6]        
        self.condition = 'dynamic'
        self.target_count = 0
        self.n = 6
        self.start = True
        self.time = None
        self.button_list = []
        self.text = Label(self.window, width=40)
        self.text.configure(anchor=CENTER)
        self.text.pack(side=TOP, fill=X)
        self.generate_random_board()
        self.create_keyboard()
        self.text.config(text = "Press any key to play")             
        
    def create_keyboard(self):
        self.keyboard = Frame(self.window)
        self.keyboard.pack(side=BOTTOM)
        
        r = 0
        c = 0
        for string in self.board:
            row = Frame(self.keyboard)
            row.grid(row=r, column=0, sticky="")
            row.grid_rowconfigure(0, weight=1)
            for ch in string:
                count = 0
                bf = Frame(row, height=32, width=32)
                bf.pack_propagate(0)
                bf.grid(row=r, column=c)
                b = Button(bf, 
                           text=ch, 
                           command=lambda x=ch: self.challenge(x))
                b.pack(fill=BOTH, expand=1)
                self.button_list.append(b)
                c += 1 
                count + 1
            c = 0
            r += 1

    def generate_random_board(self):
        self.letters = list(self.alphabet)
        random.shuffle(self.letters)       
        self.board = [self.letters[:10], self.letters[10:19], self.letters[19:]]
            
    def button_change(self):
        for string in self.board:
            for i in range(len(string)):
                ch = string[i]
                self.button_list[i].configure(text=ch, \
                                           command=lambda x=ch: self.challenge(x))
        
    def challenge(self, x):
        self.text.config(text = self.target_letters[self.target_count])
        if not self.start:
            print('start', self.time)
            if x == self.target_letters[self.target_count]:
                total_time = (time.time() - self.time)
                print('total time', total_time)
                if self.condition == 'static':                    
                    with open('experiment_static_log.csv', 'a+', newline='') as log:               
                        write_log = csv.writer(log)                    
                        write_log.writerow(["Logan", "static", self.target_letters[self.target_count], \
                                        self.n, total_time])
                else:
                    with open('experiment_dynamic_log.csv', 'a+', newline='') as log:               
                        write_log = csv.writer(log)                    
                        write_log.writerow(["Logan", "dynamic", self.target_letters[self.target_count], \
                                        self.n, total_time])                    
                self.target_count += 1
                self.time = time.time()
            
                if self.target_count == len(self.target_letters):
                    random.shuffle(self.target_letters)
                    self.target_count = 0
                    self.n -= 1 
                if self.condition == 'dynamic':
                    self.keyboard.destroy()
                    self.generate_random_board()
                    self.create_keyboard()
                self.text.config(text = self.target_letters[self.target_count])
            
            if self.n == 0:
                self.text.config(text="Challenge Completed")
                self.game_over = True         
        else:
            self.start = False
            self.time = time.time()
                
               
   
def main():
    window = Tk()
    experiment = KeyboardGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()