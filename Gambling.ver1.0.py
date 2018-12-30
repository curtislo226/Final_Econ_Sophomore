import csv
import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep
import datetime

import random


def RandomRoll(number):
    out = random.uniform(0, 100)
    return out


def profit(BetAmount, Payout):
    ProfitOnWin = (BetAmount * Payout) - BetAmount
    return ProfitOnWin


money = float(100)
Number = float(0)

BetAmount = float(10.0)
BetNow = BetAmount

Payout = float(2.0)
WinChance = float(99.0 / Payout)
RollUnderToWin = WinChance

ProfitOnWin = profit(BetAmount, Payout)


# 主頁

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

        self.frame = StartPage(parent=container, controller=self)

        self.frame.grid(row=0, column=0, sticky="nsew")

    def show_roll(self):
        self.t = Roll_Page(self.frame)


# 開始頁面

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.config(bg="ivory3")
        self.controller = controller
        self.grid()
        self.createUser()

    def createUser(self):

       #--------------------------------------------------------------#
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)
        f2 = tkfont.Font(size=15, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#
        f3 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f4 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
        f5 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#
        f6 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f7 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#
        f8 = tkfont.Font(size=20, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#
        f9 = tkfont.Font(size=11, family="Fixdsys", weight=tkfont.BOLD)
        f10 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#

       #---USERNAME,MONEY---#

        self.lblname = tk.Label(self, text="Username",
                                font=f1, height=1, width=15)
        self.lblmoney = tk.Label(
            self, text="Money", font=f1, height=1, width=15)

        self.moneystr = tk.StringVar()
        self.moneystr.set(str(money))
        self.Mymoney = tk.Label(self, textvariable=self.moneystr, font=f2)

        self.username = tk.Entry(self, font=f2)

       #---第二層(BetAmount,ProfitOnWin)---#

        # BetAmount 宣告
        self.BetAmountstr = tk.StringVar()
        self.BetAmountstr.set("10.0")

        self.lblBet = tk.Label(self, text="BET AMOUNT",
                               font=f3, height=2, width=49)
        self.txtDebt = tk.Entry(self, font=f4, textvariable=self.BetAmountstr)

        BetAmount = float(self.BetAmountstr.get())

        # BetAmount button 宣告
        self.btnhalf = tk.Button(
            self, text="1/2", command=self.BetHalf, font=f5, height=1, width=16)
        self.btndouble = tk.Button(
            self, text="x2", command=self.BetDouble, font=f5, height=1, width=16)
        self.btnmax = tk.Button(
            self, text="MAX", command=self.BetMax, font=f5, height=1, width=15)

       #---第三層(PAYOUT,RollUnderToWin,WinChance)---#

        self.payoutstr = tk.StringVar()
        self.payoutstr.set("2.0")

        self.lblPay = tk.Label(self, text="PAYOUT",
                               height=3, width=20, font=f6)
        self.txtpayout = tk.Entry(self, font=f7, textvariable=self.payoutstr)

        Payout = float(self.txtpayout.get())

        WinChance = float(99 / Payout)

        self.WinChancestr = tk.StringVar()
        self.WinChancestr.set(str(WinChance))

        self.lblUnderwin = tk.Label(
            self, text="ROLL UNDER TO WIN", height=3, width=20, font=f6)
        self.lblundernum = tk.Label(
            self, font=f7, textvariable=self.WinChancestr)

        self.lblChance = tk.Label(
            self, text='WIN CHANCE%', font=f6, height=3, width=30)
        self.lblchange = tk.Label(
            self, textvariable=self.WinChancestr, height=2, width=30, font=f6)

       #---第二層ProfitOnWin---#

        self.ProfitOnWinstr = tk.StringVar()
        self.ProfitOnWinstr.set(str(BetAmount * (Payout - 1)))

        self.lblProfit = tk.Label(
            self, text="PROFIT ON WIN", font=f5, height=2, width=50)
        self.Profit = tk.Label(
            self, textvariable=self.ProfitOnWinstr, font=f3, height=2, width=50, bg='white')

       #---第四層(ONWIN,ONLOSE)---#

        self.lblLose = tk.Label(self, text="ON LOSE",
                                font=f9, height=3, width=35)
        self.lblWin = tk.Label(self, text="ON WIN",
                               font=f9, height=3, width=35)
        self.btnLreset = tk.Button(
            self, text="RESET TO BASE", font=f9, height=2, width=18, command=self.OnloseRB)
        self.btnLincrease = tk.Button(
            self, text="INCRASE BY", font=f9, height=2, width=18, command=self.OnloseIC)
        self.txtLnum = tk.Entry(self, font=f10)
        self.btnWreset = tk.Button(
            self, text="RESET TO BASE", font=f9, height=2, width=18, command=self.OnwinRB)
        self.btnWincrease = tk.Button(
            self, text="INCREASE BY", font=f9, height=2, width=18, command=self.OnwinIC)
        self.txtWnum = tk.Entry(self, font=f10)
        self.btnLreset["relief"] = "sunken"
        self.btnWreset["relief"] = "sunken"
        self.txtLnum.insert(tk.END, "0.0")
        self.txtWnum.insert(tk.END, "0.0")

       #---BetNow設定---#

       #---最底層ROLL,AUTO---#

        self.btnroll = tk.Button(
            self, text="ROLL", command=self.ROLL, font=f8, height=1, width=18, bg="ivory3")
        self.btnauto = tk.Button(
            self, text="Auto", font=f8, height=1, width=18, bg="ivory3", command=lambda: self.controller.show_roll())

        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblname.place(x=100, y=10)
        self.lblmoney.place(x=300, y=10)
        self.username.place(x=200, y=10, width=75)
        self.Mymoney.place(x=400, y=10, width=300)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblBet.place(x=100, y=60)
        self.lblProfit.place(x=600, y=60)
        self.txtDebt.place(x=100, y=100)
        self.Profit.place(x=600, y=100)
        self.btnhalf.place(x=100, y=150)
        self.btndouble.place(x=253, y=150)
        self.btnmax.place(x=406, y=150)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblUnderwin.place(x=100, y=200)
        self.lblundernum.place(x=100, y=250, width=185)
        self.lblPay.place(x=500, y=200)
        self.txtpayout.place(x=500, y=250, width=185)
        self.lblChance.place(x=800, y=200)
        self.lblchange.place(x=800, y=250)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblLose.place(x=160, y=320)
        self.lblWin.place(x=660, y=320)
        self.btnLreset.place(x=100, y=370)
        self.btnLincrease.place(x=253, y=370)
        self.txtLnum.place(x=415, y=370, width=100)
        self.btnWreset.place(x=600, y=370)
        self.btnWincrease.place(x=753, y=370)
        self.txtWnum.place(x=905, y=370, width=100)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.btnroll.place(x=200, y=450)
        self.btnauto.place(x=600, y=450)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

    # 所有button函式
    def BetHalf(self):

        global BetAmount
        global BetNow

        self.BetAmountstr.set(str(BetAmount * 0.5))
        BetAmount *= 0.5
        BetNow = BetAmount
        ProfitOnWin = profit(BetAmount, Payout)
        self.ProfitOnWinstr.set(str(ProfitOnWin))

    def BetDouble(self):

        global BetAmount
        global BetNow

        if (BetAmount * 2 > money):
            self.BetAmountstr.set(str(money))
            BetAmount = money
            BetNow = BetAmount
            ProfitOnWin = profit(BetAmount, Payout)
            self.ProfitOnWinstr.set(str(ProfitOnWin))
        else:
            self.BetAmountstr.set(str(BetAmount * 2))
            BetAmount *= 2
            BetNow = BetAmount
            ProfitOnWin = profit(BetAmount, Payout)
            self.ProfitOnWinstr.set(str(ProfitOnWin))

    def BetMax(self):

        global BetAmount
        global BetNow

        self.BetAmountstr.set(str(money))
        BetAmount = money
        BetNow = BetAmount
        ProfitOnWin = profit(BetAmount, Payout)
        self.ProfitOnWinstr.set(str(ProfitOnWin))

    def OnloseRB(self):
        self.btnLreset["relief"] = "sunken"
        self.btnLincrease["relief"] = "raised"

    def OnloseIC(self):
        self.btnLreset["relief"] = "raised"
        self.btnLincrease["relief"] = "sunken"

    def OnwinRB(self):
        self.btnWreset["relief"] = "sunken"
        self.btnWincrease["relief"] = "raised"

    def OnwinIC(self):
        self.btnWreset["relief"] = "raised"
        self.btnWincrease["relief"] = "sunken"

        #-----ROLL-----#

    def ROLL(self):

        global money
        global BetAmount

        BetAmount = float(self.txtDebt.get())
        Payout = float(self.txtpayout.get())
        BetNow = BetAmount

        WinChance = float(99 / Payout)
        self.WinChancestr.set(str(WinChance))

        self.ProfitOnWinstr.set(str(BetAmount * (Payout - 1)))

        money -= BetNow
        RollNumber = random.uniform(0, 100)

        print(RollNumber)

        if RollNumber < 49.5:

            money += BetNow * Payout
            self.moneystr.set(str(money))

        else:

            self.moneystr.set(str(money))

# 執行結果在這個頁面顯示


class Roll_Page(tk.Toplevel):

    def __init__(self, data):
        tk.Toplevel.__init__(self)
        self.createResultTitle(data)	# roll_page標題
        self.createLabels()				# 存放執行結果的labels
        self.get_data(data)				# 把StartPage選擇好的狀態抓下來
        self.after(500, self.refresh)	# 重複更新

    def get_data(self, data):
        self.money = float(data.moneystr.get())							# 使用者持有金錢
        self.originbet = self.bet = float(data.BetAmountstr.get())		# 使用者的賭金
        self.rollnum = float(data.WinChancestr.get())					# 目標數字
        self.payout = float(data.payoutstr.get())						# 賠率
        if data.btnLreset["relief"] == "sunken":						# 檢測使用者有沒有選擇retrurn to base
            self.LRB = True
        else:
            self.LRB = False
            self.LIC = float(data.txtLnum.get())
        if data.btnWreset["relief"] == "sunken":
            self.WRB = True
        else:
            self.WRB = False
            self.WIC = float(data.txtWnum.get())

    def createResultTitle(self, data):
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)

        self.ghost = tk.Label(self, text="", font=f1, height=2, width=18)			# 下面都是標題宣告
        self.lbltime = tk.Label(self, text="Time", font=f1, height=2, width=18)
        self.lblbet = tk.Label(self, text="Bet", font=f1, height=2, width=18)
        self.lblmul = tk.Label(self, text="Multiplier",
                               font=f1, height=2, width=18)
        self.lblgame = tk.Label(self, text="Game", font=f1, height=2, width=18)
        self.lblroll = tk.Label(self, text="Roll", font=f1, height=2, width=18)
        self.lblprofit = tk.Label(
            self, text="Profit", font=f1, height=2, width=18)
        self.btnstop = tk.Button(self, text="Stop", font=f1,						# Stop按鈕，只有按了之後，money才會回傳
                                 height=2, width=18, command=lambda: self.stop(data))

        self.ghost.grid(row=0, column=0, sticky=tk.SW + tk.NE)
        self.lbltime.grid(row=1, column=0, sticky=tk.SW + tk.NE)
        self.lblbet.grid(row=1, column=1, sticky=tk.SW + tk.NE)
        self.lblmul.grid(row=1, column=2, sticky=tk.SW + tk.NE)
        self.lblgame.grid(row=1, column=3, sticky=tk.SW + tk.NE)
        self.lblroll.grid(row=1, column=4, sticky=tk.SW + tk.NE)
        self.lblprofit.grid(row=1, column=5, sticky=tk.SW + tk.NE)
        self.btnstop.grid(row=0, column=6, sticky=tk.SW + tk.NE)

    def stop(self, data):															# stop按鈕函式宣告
        data.moneystr.set(str(self.money))											# 把money資料回傳
        self.destroy()

    def createLabels(self):															# 宣告存放執行結果的labels,放在二維list裡
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)
        self.labels = [[tk.Label(self, text="", font=f1, height=2, width=18)
                        for j in range(6)] for i in range(5)]
        for i in range(5):
            for j in range(6):
                self.labels[i][j].grid(
                    row=i + 2, column=j, sticky=tk.SW + tk.NE)

    def refresh(self):																# 更新資料函式宣告
        for i in range(4, 0, -1):													# 首先把每一行的資料都平行向下一格
            for j in range(6):
                self.labels[i][j]["text"] = self.labels[i - 1][j].cget("text")

        self.labels[0][0][															# 第一格更新時間
            "text"] = datetime.datetime.now().strftime("%H:%M:%S")
        self.labels[0][1]["text"] = str(round(self.bet, 8))							# 更新賭金
        self.labels[0][2]["text"] = str(round(self.payout, 8))						# 更新賠率
        self.labels[0][3]["text"] = "<" + str(self.rollnum)							# 更新目標數字

        rand = random.uniform(0, 100)												# 骰色子 
        self.labels[0][4]["text"] = str(round(rand, 2))

        self.money -= self.bet 														# 先付賭金
        profit = 0.0																# 本回的利潤

        if rand <= self.rollnum:													# 贏的話
            self.money += self.bet * self.payout 									# 金錢加上 (賭金 * 賠率)
            profit = self.bet * (self.payout - 1)									# 利潤為 (賭金 * (賠率 - 1))
            if self.WRB:															# 如果reutrn to base
                self.bet = self.originbet											# 讓賭金回復原樣
            else:
                self.bet *= self.WIC 												# 否則讓賭金乘上贏之後要加賭的倍率

        else:																		# 輸的話
            profit = -self.bet 														# 利潤為 (-賭金)
            if self.LRB:															# 如果reutrn to base
                self.bet = self.originbet											# 讓賭金回復原樣
            else:
                self.bet *= self.LIC 												# 否則讓賭金乘上輸之後要加賭的倍率

        self.labels[0][5]["text"] = str(											# 把profit更新
            round(profit, 8))

        self.after(500, self.refresh)												# 再更新一次


if __name__ == "__main__":
    app = SampleApp()
    app.title("Gambling")
    app.mainloop()
