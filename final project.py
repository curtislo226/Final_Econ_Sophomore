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
    #尚未解決問題:
    #需要一個背景
    #需要改字體顏色
    #第三層需要按鈕反白
    #要寫第二個介面
    
    #底下分的層數同圖片分三上中下三個部分
    def createTop(self):

        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f3 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
       
        self.lblBet = tk.Label(self, text = "BET AMOUNT", font = f1, height = 2, width = 60)                
        self.lblProfit = tk.Label(self, text = "PROFIT ON WIN", font = f1, height = 2, width = 60)
        self.txtDebt = tk.Text(self, font = f2, height = 1, width = 60)
        self.txtProfit = tk.Text(self, font = f2,height = 1, width = 60)
        self.btnhalf = tk.Button(self, text = "1/2", font = f3, height = 1, width = 18) 
        self.btndouble = tk.Button(self, text = "x2", font = f3, height = 1, width = 18) 
        self.btnmax = tk.Button(self, text = "MAX", font = f3, height = 1, width = 18)

        self.lblBet.grid(column = 0, row = 0, columnspan = 3, sticky = tk.SW + tk.NE)
        self.lblProfit.grid(column = 4, row = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtDebt.grid(column = 0, row = 1, columnspan = 3, sticky = tk.SW + tk.NE)
        self.txtProfit.grid(column = 4, row = 1, columnspan = 2, sticky = tk.SW + tk.NE)
        self.btnhalf.grid(column = 0, row = 3, sticky = tk.SW + tk.NE)
        self.btndouble.grid(column = 1, row = 3, sticky = tk.SW + tk.NE)
        self.btnmax.grid(column = 2, row = 3, sticky = tk.SW + tk.NE)

   
    def createMid(self): 
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.lblUnderwin = tk.Label(self, text = "ROLL UNDER TO WIN", height = 3, width = 30, font = f1)
        self.lblundernum = tk.Label(self, text = "待定", height = 2, width = 30, font = f2)
        self.lblPay = tk.Label(self, text = "PAYOUT", height = 3, width = 30, font = f1)
        self.txtpaynum = tk.Text(self, font = f2, height = 2, width = 30)
        self.lblChance = tk.Label(self, text = "WIN CAHNCE %", font = f1, height = 3, width = 30)
        self.txtchance = tk.Text(self, font = f2, height = 2, width = 30)
    
        self.lblUnderwin.grid(row = 4, column = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblundernum.grid(row = 5, column = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblPay.grid(row = 4 , column = 2, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtpaynum.grid(row = 5 , column = 2, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblChance.grid(row = 4 ,column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtchance.grid(row = 5 , column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
    def createBot(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)

        self.lblLose = tk.Label(self, text = "ON LOSE", font = f1, height = 3, width = 56)
        self.lblWin = tk.Label(self, text = "ON WIN", font = f1, height = 3, width = 56)
        self.btnLreset = tk.Button(self, text = "RESET TO BASE", font =f1, height = 3, width = 18)
        self.btnLincrease = tk.Button(self, text = "INCRASE BY", font =f1, height = 3, width = 18)
        self.txtLnum = tk.Text(self, font = f2, height = 3, width = 18)
        self.btnWreset = tk.Button(self, text = "RESET TO BASE", font =f1, height = 3, width = 18)
        self.btnWincrease = tk.Button(self, text = "INCREASE BY", font =f1, height = 3, width = 18)
        self.txtWnum = tk.Text(self, font = f2, height = 3, width = 18)
        
        self.lblLose.grid(row = 6, column = 0, columnspan = 3, sticky = tk.SW + tk.NE)
        self.lblWin.grid(row = 6, column = 3, columnspan = 3, sticky = tk.SW + tk.NE)
        self.btnLreset.grid(row = 7, column = 0, sticky = tk.SW + tk.NE)
        self.btnLincrease.grid(row = 7, column = 1, sticky = tk.SW + tk.NE)
        self.txtLnum.grid(row = 7, column = 2, sticky = tk.SW + tk.NE)
        self.btnWreset.grid(row = 7, column = 3, sticky = tk.SW + tk.NE)
        self.btnWincrease.grid(row = 7, column = 4, sticky = tk.SW + tk.NE)
        self.txtWnum.grid(row = 7, column = 5, sticky = tk.SW + tk.NE)
    def auto(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        self.btnauto = tk.Button(self, text = "AUTO", font =f1, height = 2, width = 15)
        
        self.btnauto.grid(row =8, column =3)
        
menu = Mainpage()
menu.master.title("Gambling")
menu.mainloop()

