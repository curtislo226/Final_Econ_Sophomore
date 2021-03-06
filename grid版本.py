import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Mainpage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createTop()                        # 主頁最上面 row = 1 ~ 3
        self.createMid()                        # 主頁中間 row = 4 ~ 5
        self.createBot()                        # 主頁最下面 row = 6 ~ 7
        self.auto()                             # auto 按鍵的按鈕
        self.createUser()                       # 使用者資料
        self.createResultTitle()                # 執行結果的標題
    #尚未解決問題:
    #需要一個背景
    #需要改字體顏色
    #第三層需要按鈕反白
    #要寫第二個介面
    #底下分的層數同圖片分三上中下三個部分
    def createUser(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.lblname = tk.Label(self, text = "Username", font = f1, height = 1, width = 15)
        self.lblmoney = tk.Label(self, text = "Money", font = f1, height = 1, width = 15)
        self.Mymoney = tk.Label(self, text = "0.0", font = f1, height = 1, width = 4)
        self.username = tk.Text(self, font = f1, height = 1, width = 15)
        
        self.lblname.grid(column = 6, row = 0, sticky = tk.SW + tk.NE)
        self.lblmoney.grid(column = 6, row = 1, sticky = tk.SW + tk.NE)
        self.username.grid(column = 7, row = 0, sticky = tk.SW + tk.NE)
        self.Mymoney.grid(column = 7, row = 1, sticky = tk.SW + tk.NE)
        
    def createTop(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f3 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
       
        self.lblBet = tk.Label(self, text = "BET AMOUNT", font = f1, height = 2, width = 60)                # 賭金標題label 宣告
        self.lblProfit = tk.Label(self, text = "PROFIT ON WIN", font = f1, height = 2, width = 60)          # 利潤標題label 宣告
        self.txtDebt = tk.Text(self, font = f2, height = 1, width = 60)                                     # 賭金內容txt 宣告
        self.Profit = tk.Label(self, text = "待改變", font = f2, height = 1, width = 60)                    # 利潤內容label 宣告
        self.btnhalf = tk.Button(self, text = "1/2", font = f3, height = 1, width = 18)                     # 賭金除以二button 宣告
        self.btndouble = tk.Button(self, text = "x2", font = f3, height = 1, width = 18)                    # 賭金乘以二button 宣告
        self.btnmax = tk.Button(self, text = "MAX", font = f3, height = 1, width = 18)                      # 賭金成為最大值button 宣告

        self.lblBet.grid(row = 0, column = 0, columnspan = 3, sticky = tk.SW + tk.NE)
        self.lblProfit.grid(row = 0, column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtDebt.grid(row = 1, column = 0, columnspan = 3, sticky = tk.S + tk.N)
        self.Profit.grid(row = 1, column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.btnhalf.grid(row = 3, column = 0, sticky = tk.SW + tk.NE)
        self.btndouble.grid(row = 3, column = 1, sticky = tk.SW + tk.NE)
        self.btnmax.grid(row = 3, column = 2, sticky = tk.SW + tk.NE)

   
    def createMid(self): 
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        f2 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.lblUnderwin = tk.Label(self, text = "ROLL UNDER TO WIN", height = 3, width = 30, font = f1)
        self.txtundernum = tk.Text(self, font = f2, height = 2, width = 30)
        self.lblPay = tk.Label(self, text = "PAYOUT", height = 3, width = 30, font = f1)
        self.txtpaynum = tk.Text(self, font = f2, height = 2, width = 30)
        self.lblChance = tk.Label(self, text = "WIN CAHNCE %", font = f1, height = 3, width = 30)
        self.lblchance = tk.Label(self, text = "待定", height = 2, width = 30, font = f2)
    
        self.lblUnderwin.grid(row = 4, column = 0, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtundernum.grid(row = 5, column = 0, columnspan = 2, sticky = tk.S + tk.N)
        self.lblPay.grid(row = 4 , column = 2, columnspan = 2, sticky = tk.SW + tk.NE)
        self.txtpaynum.grid(row = 5 , column = 2, columnspan = 2, sticky = tk.S + tk.N)
        self.lblChance.grid(row = 4 ,column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.lblchance.grid(row = 5 , column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
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
        self.lblWin.grid(row = 6, column = 4, columnspan = 2, sticky = tk.SW + tk.NE)
        self.btnLreset.grid(row = 7, column = 0, sticky = tk.SW + tk.NE)
        self.btnLincrease.grid(row = 7, column = 1, sticky = tk.SW + tk.NE)
        self.txtLnum.grid(row = 7, column = 2, sticky = tk.SW + tk.NE)
        self.btnWreset.grid(row = 7, column = 3, sticky = tk.SW + tk.NE)
        self.btnWincrease.grid(row = 7, column = 4, sticky = tk.SW + tk.NE)
        self.txtWnum.grid(row = 7, column = 5, sticky = tk.SW + tk.NE)
        
    def auto(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        self.btnroll = tk.Button(self, text = "ROLL", font =f1, height = 2, width = 15)
        self.btnauto = tk.Button(self, text = "Auto", font =f1, height = 2, width = 15)
        
        self.btnroll.grid(row =8, column =3)
        self.btnauto.grid(row =8, column =4)
        
    def createResultTitle(self):
        f1 = tkFont.Font(size = 10, family = "Fixdsys", weight=tkFont.BOLD)
        
        self.ghost = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lbltime = tk.Label(self, text="Time", font=f1, height=2, width=18)
        self.lblbet = tk.Label(self, text="Bet", font=f1, height=2, width=18)
        self.lblmul = tk.Label(self, text="Multiplier", font=f1, height=2, width=18)
        self.lblgame = tk.Label(self, text="Game", font=f1, height=2, width=18)
        self.lblroll = tk.Label(self, text="Roll", font=f1, height=2, width=18)
        self.lblprofit = tk.Label(self, text="Profit", font=f1, height=2, width=18)
        
        self.ghost.grid(row = 9, column = 0, sticky = tk.SW + tk.NE)
        self.lbltime.grid(row = 10, column = 0, sticky = tk.SW + tk.NE)
        self.lblbet.grid(row = 10, column = 1, sticky = tk.SW + tk.NE)
        self.lblmul.grid(row = 10, column = 2, sticky = tk.SW + tk.NE)
        self.lblgame.grid(row = 10, column = 3, sticky = tk.SW + tk.NE)
        self.lblroll.grid(row = 10, column = 4, sticky = tk.SW + tk.NE)
        self.lblprofit.grid(row = 10, column = 5, sticky = tk.SW + tk.NE)
        
menu = Mainpage()
menu.master.title("Gambling")
menu.mainloop()

