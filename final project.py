import csv
import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk

###函數設定###

import random

def RandomRoll(number) :
    out = random.uniform(0,100)
    return out
#隨機轉出0-100之間的小數數字

def profit(BetAmount,Payout) :
    ProfitOnWin = (BetAmount*Payout) - BetAmount
    return ProfitOnWin
#獲勝利潤	
	
def BetHalf(BetAmount) :
    BetAmount *= 0.5
    return BetAmount
#改下一半,"bh"
	
	
def BetDouble(BetAmount) :
    BetAmount *= 2
    if BetAmount > money :
        BetAmount = money
    return BetAmount
#改下2倍,"bd"
	
	
def BetMax(BetAmount) :
    BetAmount = money
    return BetAmount
#全押,"bm"

def IncreaseBy(BetNow,percent) :		
    BetNow += BetNow * percent
    return BetNow
#輸/贏時加注

###預設各項參數###

money = float(100)
Number = float(0)

BetAmount = float(20.0)
BetNow = BetAmount

Payout = float(2.0) 
WinChance = float(99.0/Payout)
RollUnderToWin = WinChance

ProfitOnWin = profit(BetAmount,Payout)
MaxBet = float(10000000)
MinBet = float(0.00000001)

LoseType = "B"
OnLosePercent = float(1) 

WinType = "A" 
OnWinPercent = float(0) 


class SampleApp(tk.Tk):
    # initialization

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default='Pixelpress-Pirates-Flag-Jolly-Roger.ico')
        # tk.Tk.wm_title(self, "NTU_Econ_game")

        self.minsize(width=1100, height=600)
        self.maxsize(width=1100, height=600)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # 有製作任何新的頁面就加進這個for loop 裡面
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# 在button mutiple command 裡面負責轉換page


def showNextFrame(self, page):
    self.controller.show_frame(page)

# 這個不用看


class StartPage1(tk.Frame):
    # initialization

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tkfont.Font(family='STLiti', size=72, weight="bold")
        label = tk.Label(self, text="NTU ECON Game", font=f1, fg="#a2cffe")
        label.pack(side="top", pady=100)
        f1 = ttk.Style()
        f1.configure('my.TButton', font=(
            'Bahnschrift SemiBold SemiConden', 24))
        self.btn1 = ttk.Button(self, text="Start Game", width=15,
                               command=lambda: controller.show_frame("PageOne"))
        self.btn1.place(x=520, y=550)

# 開始頁面

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="ivory3")
        self.controller = controller
        self.grid()
        self.createTop()                        # 主頁最上面 row = 1 ~ 3
        self.createMid()                        # 主頁中間 row = 4 ~ 5
        self.createBot()                        # 主頁最下面 row = 6 ~ 7
        self.auto()                             # auto 按鍵的按鈕
        self.createUser()                       # 使用者資料
        self.btn1 = ttk.Button(self, text="Start Game", width=15,
                               command=lambda: controller.show_frame("PageOne"))
        self.btn1.place(x=520, y=550)
    # 尚未解決問題:
    # 需要一個背景
    # 需要改字體顏色
    # 第三層需要按鈕反白
    # 要寫第二個介面
    # 底下分的層數同圖片分三上中下三個部分

    def createUser(self):
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)

        self.lblname = tk.Label(self, text="Username",
                                font=f1, height=1, width=15)
        self.lblmoney = tk.Label(
            self, text="Money", font=f1, height=1, width=15)
        self.Mymoney = tk.Label(self, text=str(money), font=f1, height=1, width=4)
        self.username = tk.Text(self, font=f1, height=1, width=15)

        self.lblname.place(x=100, y=10)
        self.lblmoney.place(x = 300, y = 10)
        self.username.place(x = 200, y = 10)
        self.Mymoney.place(x = 400, y = 10)

    def createTop(self):
        f1 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f2 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
        f3 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)

        # 賭金標題label 宣告
        self.lblBet = tk.Label(self, text="BET AMOUNT",
                               font=f1, height=2, width=49)
        # 利潤標題label 宣告
        self.lblProfit = tk.Label(
            self, text="PROFIT ON WIN", font=f1, height=2, width=50)          
        # 賭金內容txt 宣告
        self.txtDebt = tk.Entry(self, font=f2)
        # 利潤內容label 宣告
        self.Profit = tk.Label(self, text=str(ProfitOnWin), font=f1, height=2, width=50, bg='white')
        # 賭金除以二button 宣告
        self.btnhalf = tk.Button(self, text="1/2", font=f3, height=1, width=16)
        # 賭金乘以二button 宣告
        self.btndouble = tk.Button(
            self, text="x2", font=f3, height=1, width=16)
        # 賭金成為最大值button 宣告
        self.btnmax = tk.Button(self, text="MAX", font=f3, height=1, width=15)

        self.lblBet.place(x = 100, y = 60)
        self.lblProfit.place(x = 600, y = 60)
        self.txtDebt.place(x = 100, y = 100)
        self.Profit.place(x = 600, y = 100)
        self.btnhalf.place(x = 100, y = 150)
        self.btndouble.place(x = 253, y = 150)
        self.btnmax.place(x = 406, y = 150)

    def createMid(self):
        f1 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f2 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)

        self.lblUnderwin = tk.Label(
            self, text="ROLL UNDER TO WIN", height=3, width=20, font=f1)
        self.txtundernum = tk.Entry(self, font=f2)
        self.lblPay = tk.Label(self, text="PAYOUT",
                               height=3, width=20, font=f1)
        self.txtpaynum = tk.Entry(self, font=f2)
        self.lblChance = tk.Label(
            self, text="WIN CAHNCE %", font=f1, height=3, width=30)
        self.lblchance = tk.Label(self, text="123", height=2, width=30, font=f1)

        self.lblUnderwin.place(x = 100, y = 200)
        self.txtundernum.place(x = 100, y = 250, width=185)
        self.lblPay.place(x = 500, y = 200)
        self.txtpaynum.place(x = 500, y = 250, width=185)
        self.lblChance.place(x = 800, y = 200)
        self.lblchance.place(x = 800, y = 250)

    def createBot(self):
        f1 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f2 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)

        self.lblLose = tk.Label(self, text="ON LOSE",
                                font=f1, height=3, width=35)
        self.lblWin = tk.Label(self, text="ON WIN",
                               font=f1, height=3, width=35)
        self.btnLreset = tk.Button(
            self, text="RESET TO BASE", font=f1, height=2, width=18)
        self.btnLincrease = tk.Button(
            self, text="INCRASE BY", font=f1, height=2, width=18)
        self.txtLnum = tk.Entry(self, font=f2)
        self.btnWreset = tk.Button(
            self, text="RESET TO BASE", font=f1, height=2, width=18)
        self.btnWincrease = tk.Button(
            self, text="INCREASE BY", font=f1, height=2, width=18)
        self.txtWnum = tk.Entry(self, font=f2)

        self.lblLose.place(x = 160, y = 320)
        self.lblWin.place(x = 660, y = 320)
        self.btnLreset.place(x = 100, y = 370)
        self.btnLincrease.place(x = 253, y = 370)
        self.txtLnum.place(x = 415, y = 370, width=100)
        self.btnWreset.place(x = 600, y = 370)
        self.btnWincrease.place(x = 753, y = 370)
        self.txtWnum.place(x = 905, y = 370, width=100)

    def auto(self):
        f1 = tkfont.Font(size=20, family="Fixdsys", weight=tkfont.BOLD)
        self.btnroll = tk.Button(
            self, text="ROLL", font=f1, height=1, width=18, bg="ivory3")
        self.btnauto = tk.Button(
            self, text="Auto", font=f1, height=1, width=18, bg="ivory3")

        self.btnroll.place(x = 200, y = 450)
        self.btnauto.place(x = 600, y = 450)

# 第一頁

class PageOne(tk.Frame):
    # initialization

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createResultTitle()

    def createResultTitle(self):
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)

        self.ghost = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lbltime = tk.Label(self, text="Time", font=f1, height=2, width=18)
        self.lblbet = tk.Label(self, text="Bet", font=f1, height=2, width=18)
        self.lblmul = tk.Label(self, text="Multiplier",
                               font=f1, height=2, width=18)
        self.lblgame = tk.Label(self, text="Game", font=f1, height=2, width=18)
        self.lblroll = tk.Label(self, text="Roll", font=f1, height=2, width=18)
        self.lblprofit = tk.Label(
            self, text="Profit", font=f1, height=2, width=18)

        self.ghost.grid(row=9, column=0, sticky=tk.SW + tk.NE)
        self.lbltime.grid(row=10, column=0, sticky=tk.SW + tk.NE)
        self.lblbet.grid(row=10, column=1, sticky=tk.SW + tk.NE)
        self.lblmul.grid(row=10, column=2, sticky=tk.SW + tk.NE)
        self.lblgame.grid(row=10, column=3, sticky=tk.SW + tk.NE)
        self.lblroll.grid(row=10, column=4, sticky=tk.SW + tk.NE)
        self.lblprofit.grid(row=10, column=5, sticky=tk.SW + tk.NE)


if __name__ == "__main__":
    app = SampleApp()
    app.title("NTU ECON Game")
    app.mainloop()