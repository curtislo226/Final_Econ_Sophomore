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
        # self.auto()
    #尚未解決問題:
    #目前總共有8ROW跟7COLUMN    
    #可是我調整的WIDTH跟GRID跟預期的不一樣
    #需要一個背景
    #需要改字體顏色
    #第三層需要按鈕反白
    #要寫第二個介面
    
    #底下分的層數同圖片分三上中下三個部分
    def createTop(self):

        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f3 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
       
        self.lblBet = tk.Label(self, text = "BET AMOUNT", font = f1, height = 1, width = 60) 
        self.lblProfit = tk.Label(self, text = "PROFIT ON WIN", font = f1, height = 1, width = 60)
        self.txtDebt = tk.Text(self, font = f2, height = 1, width = 60)
        self.txtProfit = tk.Text(self, font = f2,height = 1, width = 60)
        self.half = tk.Button(self, text = "1/2", font = f3, height = 1, width = 18) 
        self.double = tk.Button(self, text = "x2", font = f3, height = 1, width = 18) 
        self.max = tk.Button(self, text = "MAX", font = f3, height = 1, width = 18) 

        self.lblBet.grid(column = 0, row = 0, columnspan = 3, sticky = tk.SW + tk.NE)
        self.lblProfit.grid(column = 4, row = 0, sticky = tk.SW + tk.NE)
        self.txtDebt.grid(column = 0, row = 1, columnspan = 3, sticky = tk.SW + tk.NE)
        self.txtProfit.grid(column = 4, row = 1, sticky = tk.SW + tk.NE)
        self.half.grid(column = 0, row = 3, sticky = tk.SW + tk.NE)
        self.double.grid(column = 1, row = 3, sticky = tk.SW + tk.NE)
        self.max.grid(column = 2, row = 3, sticky = tk.SW + tk.NE)
   
    def createMid(self): 
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.lblUnderwin = tk.Label(self, text = "ROLL UNDER TO WIN", height = 2, width = 30, font = f1)
        self.undernum = tk.Label(self, text = "待定", height = 1, width = 30, font = f2)
        self.lblPay = tk.Label(self, text = "PAYOUT", height = 2, width = 30, font = f1)
        self.paynum = tk.Text(self, font = f2, height = 1, width = 30)
        self.lblChance = tk.Label(self, text = "WIN CAHNCE %", font = f1, height = 2, width = 30)
        self.chance = tk.Text(self, font = f2, height = 1, width = 30)
    
        self.lblUnderwin.grid(row = 4, column = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.undernum.grid(row = 5, column = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblPay.grid(row = 4 , column = 2, columnspan = 2, sticky = tk.SW + tk.NE)
        self.paynum.grid(row = 5 , column = 2, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblChance.grid(row = 4 ,column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.chance.grid(row = 5 , column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
    def createBot(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)

        self.lblLose = tk.Label(self, text = "ON LOSE", font = f1, height = 2, width = 56)
        self.lblWin = tk.Label(self, text = "ON WIN", font = f1, height = 2, width = 56)
        self.Lreset = tk.Button(self, text = "RESET TO BASE", font =f1, height = 2, width = 18)
        self.Lincrease = tk.Button(self, text = "INCRASE BY", font =f1, height = 2, width = 18)
        self.Lnum = tk.Text(self, font = f2, height = 2, width = 18)
        self.Wreset = tk.Button(self, text = "RESET TO BASE", font =f1, height = 2, width = 18)
        self.Wincrease = tk.Button(self, text = "INCREASE BY", font =f1, height = 2, width = 18)
        self.Wnum = tk.Text(self, font = f2, height = 2, width = 18)
        
        self.lblLose.grid(row = 6, column = 0, columnspan = 3, sticky = tk.SW + tk.NE)
        self.lblWin.grid(row = 6, column = 3, columnspan = 3, sticky = tk.SW + tk.NE)
        self.Lreset.grid(row = 7, column = 0, sticky = tk.SW + tk.NE)
        self.Lincrease.grid(row = 7, column = 1, sticky = tk.SW + tk.NE)
        self.Lnum.grid(row = 7, column = 2, sticky = tk.SW + tk.NE)
        self.Wreset.grid(row = 7, column = 3, sticky = tk.SW + tk.NE)
        self.Wincrease.grid(row = 7, column = 4, sticky = tk.SW + tk.NE)
        self.Wnum.grid(row = 7, column = 5, sticky = tk.SW + tk.NE)
    # def auto(self):
        # f1 = tkFont.Font(size = 2, family = "Fixdsys", weight=tkFont.BOLD)
        # self.auto = tk.Button(self, text = "AUTO", font =f1)
        
        # self.auto.grid(row =8, column =3)
menu = Mainpage()
menu.master.title("Gambling")
menu.mainloop()

