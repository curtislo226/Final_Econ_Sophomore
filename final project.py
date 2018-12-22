import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Mainpage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self) 
        self.grid()
        self.createTop()
        self.createMid()
        self.createBot()
        self.auto()
        
    def createTop(self):
        f1 = tkFont.Font(size = 15, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 25, family = "Fixdsys", weight=tkFont.BOLD)
        f3 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
       
        self.lblBet = tk.Label(self, text = "BET AMOUNT", height = 2, font = f1) 
        self.lblProfit = tk.Label(self, text = "PROFIT ON WIN", height = 2, font = f1)
        self.txtDebt = tk.Text(self, height = 1, width = 10, font = f2)
        self.txtProfit = tk.Text(self, height = 1, width = 10, font = f2)
        self.half = tk.Button(self, text = "1/2", height = 1, width = 5, font = f3) 
        self.double = tk.Button(self, text = "x2", height = 1, width = 5, font = f3) 
        self.max = tk.Button(self, text = "MAX", height = 1, width = 5, font = f3) 
        self.empty = tk.Label(self, text = "") 
        
        self.lblBet.grid(row = 0, column = 1)
        self.empty.grid(row = 0, column = 3)
        self.lblProfit.grid(row = 0, column = 4)
        self.txtDebt.grid(row = 1, column = 0, columnspan = 3, sticky = tk.NE + tk.SW) 
        self.txtProfit.grid(row = 1, column = 4, columnspan = 3, sticky = tk.NE + tk.SW)
        self.half.grid(row = 2, column = 0, sticky = tk.W + tk.E)
        self.double.grid(row = 2, column = 1, sticky = tk.W + tk.E)
        self.max.grid(row = 2, column = 2, sticky = tk.W + tk.E)
   
    def createMid(self): 
        f1 = tkFont.Font(size = 15, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 25, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.lblUnderwin = tk.Label(self, text = "ROLL UNDER TO WIN", height = 2, font = f1)
        self.undernum = tk.Label(self, text = "待定", height = 1, width = 10, font = f2)
        self.lblPay = tk.Label(self, text = "PAYOUT", height = 2, width = 20, font = f1)
        self.paynum = tk.Text(self, height = 1, width = 15, font = f2)
        self.lblChance = tk.Label(self, text = "WIN CAHNCE %", height = 2, width = 10, font = f1)
        self.chance = tk.Text(self, height = 1, width = 15, font = f2)
    
        self.lblUnderwin.grid(row = 4, column = 1, sticky = tk.W + tk.E)
        self.undernum.grid(row = 5, column = 1, sticky = tk.W + tk.E)
        self.lblPay.grid(row = 4 , column = 3, sticky = tk.W + tk.E)
        self.paynum.grid(row = 5 , column = 3, sticky = tk.W + tk.E)
        self.lblChance.grid(row = 4 ,column = 5, sticky = tk.W + tk.E)
        self.chance.grid(row = 5 , column = 5, sticky = tk.W + tk.E)
    def createBot(self):
        f1 = tkFont.Font(size = 15, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 25, family = "Fixdsys", weight=tkFont.BOLD)

        self.lblLose = tk.Label(self, text = "ON LOSE", height = 2, font = f1)
        self.lblWin = tk.Label(self, text = "ON WIN", height = 2, font = f1)
        self.resetL = tk.Button(self, text = "RESET TO BASE", height = 1, font =f1)
        self.increaseL = tk.Button(self, text = "INCRASE BY", height = 1, font =f1)
        self.Lnum = tk.Text(self, height = 1, width = 10, font = f2)
        self.resetW = tk.Button(self, text = "RESET TO BASE", height = 1, font =f1)
        self.increaseW = tk.Button(self, text = "INCREASE BY", height = 1, font =f1)
        self.Wnum = tk.Text(self, height = 1, width = 10, font = f2)
        
        self.lblLose.grid(row = 6, column = 0, sticky = tk.W)
        self.lblWin.grid(row = 6, column = 4, sticky = tk.W)
        self.resetL.grid(row = 7, column = 0, sticky = tk.W + tk.E)
        self.increaseL.grid(row = 7, column = 1, sticky = tk.W + tk.E)
        self.Lnum.grid(row = 7, column = 2, sticky = tk.W + tk.E)
        self.resetW.grid(row = 7, column = 4, sticky = tk.W + tk.E)
        self.increaseW.grid(row = 7, column = 5, sticky = tk.W + tk.E)
        self.Wnum.grid(row = 7, column = 6, sticky = tk.W + tk.E)
    def auto(self):
        f1 = tkFont.Font(size = 40, family = "Fixdsys", weight=tkFont.BOLD)
        self.auto = tk.Button(self, text = "AUTO", height = 1, font =f1)
        
        self.auto.grid(row =8, column =3)
menu = Mainpage()
menu.master.title("Gambling")
menu.mainloop()

