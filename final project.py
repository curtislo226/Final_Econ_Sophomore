import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Mainpage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createTop()
        # self.createMid()
        # self.createBot()
        
    def createTop(self):
        f1 = tkFont.Font(size = 15, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 35, family = "Fixdsys", weight=tkFont.BOLD)
        f3 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
       
        self.lblBet = tk.Label(self, text = "BET AMOUNT", height = 1, font = f1) 
        self.lblProfit = tk.Label(self, text = "PROFIT ON WIN", height = 1, font = f1)
        self.txtDebt = tk.Text(self, height = 1, width = 15, font = f2)
        self.txtProfit = tk.Text(self, height = 1, width = 15, font = f2)
        self.half = tk.Button(self, text = "1/2", height = 1, width = 15, font = f3) 
        self.double = tk.Button(self, text = "x2", height = 1, width = 5, font = f3) 
        self.max = tk.Button(self, text = "MAX", height = 1, width = 15, font = f3) 
        
        self.lblBet.grid(row = 0, column = 1)
        self.lblProfit.grid(row = 0, column = 4)
        self.txtDebt.grid(row = 1, column = 0, columnspan = 3, sticky = tk.NE + tk.SW) 
        self.txtProfit.grid(row = 1, column = 4)
        self.half.grid(row = 2, column = 0, sticky = tk.W + tk.E)
        self.double.grid(row = 2, column = 1, sticky = tk.W + tk.E)
        self.max.grid(row = 2, column = 2, sticky = tk.W + tk.E)

menu = Mainpage()
menu.master.title("Gambling")
menu.mainloop()

