import csv
import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

import random
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
        f11 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
        f12 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#
        f13 = tkfont.Font(size=30, family="Fixdsys", weight=tkfont.BOLD)
       #--------------------------------------------------------------#

       #---USERNAME,MONEY---#
        self.lblname = tk.Label(self, text="Username",                      # 輸入名字的部分
                                font=f1, height=1, width=15)

        self.username = tk.Entry(self, font=f2)

        self.lblmoney = tk.Label(                                           # 輸入金錢的部分
            self, text="Money", font=f1, height=1, width=15)
        # moneystr用來監控money的變化
        self.moneystr = tk.DoubleVar()
        self.moneystr.set(100)
        self.moneystr.trace("w", self.written_money)
        self.Mymoney = tk.Label(self, textvariable=self.moneystr, font=f2)

       #---第二層(BetAmount,ProfitOnWin)---#

        # BetAmount 宣告
        self.BetAmountstr = tk.DoubleVar()
        self.BetAmountstr.set(10.0)
        self.BetAmountstr.trace("w", self.written_bet)

        self.lblBet = tk.Label(self, text="BET AMOUNT",
                               font=f3, height=2, width=49)
        self.txtDebt = tk.Entry(self, font=f4, textvariable=self.BetAmountstr)

        # BetAmount button 宣告
        self.btnhalf = tk.Button(
            self, text="1/2", command=lambda: self.BetAmountstr.set(self.BetAmountstr.get() / 2), font=f5, height=1, width=16)
        self.btndouble = tk.Button(
            self, text="x2", command=lambda: self.BetAmountstr.set(self.BetAmountstr.get() * 2), font=f5, height=1, width=16)
        self.btnmax = tk.Button(
            self, text="MAX", command=lambda: self.BetAmountstr.set(self.moneystr.get()), font=f5, height=1, width=15)

       #---第三層(PAYOUT,RollUnderToWin,WinChance)---#

        self.payoutstr = tk.DoubleVar()                                         # 賠率的部分
        # payoutstr用來監控賠率的變化
        self.payoutstr.set(3.0)

        self.lblPay = tk.Label(self, text="PAYOUT",
                               height=3, width=20, font=f6)
        self.txtpayout = tk.Entry(self, font=f7, textvariable=self.payoutstr)
        self.payoutstr.trace("w", self.written_payout)

        self.WinChancestr = tk.DoubleVar()                                      # 勝率的部分
        # WinChancestr用來監控勝率的變化
        self.WinChancestr.set(33.00)
        self.lblUnderwin = tk.Label(
            self, text="ROLL UNDER TO WIN", height=3, width=20, font=f6)
        self.lblundernum = tk.Label(
            self, font=f7, textvariable=self.WinChancestr)

        self.lblChance = tk.Label(
            self, text='WIN CHANCE%', font=f6, height=3, width=30)
        self.lblchange = tk.Label(
            self, textvariable=self.WinChancestr, height=2, width=30, font=f6)
       #---第二層ProfitOnWin---#

        self.ProfitOnWinstr = tk.DoubleVar()                                    # 利率的部分
        self.ProfitOnWinstr.set(self.BetAmountstr.get()
                                * (self.payoutstr.get() - 1))

        self.lblProfit = tk.Label(
            self, text="PROFIT ON WIN", font=f5, height=2, width=50)
        self.Profit = tk.Label(
            self, textvariable=self.ProfitOnWinstr, font=f3, height=2, width=50, bg='white')

       #---第四層(ONWIN,ONLOSE)---#

        self.lblLose = tk.Label(self, text="ON LOSE",                           # 輸了後要做什麼的部分
                                font=f9, height=3, width=35)
        self.lblWin = tk.Label(self, text="ON WIN",
                               font=f9, height=3, width=35)

        self.btnLreset = tk.Button(
            self, text="RESET TO BASE", font=f9, height=2, width=18, command=self.OnloseRB)
        self.btnLincrease = tk.Button(
            self, text="INCRASE BY", font=f9, height=2, width=18, command=self.OnloseIC)

        self.LosePercentstr = tk.DoubleVar()
        self.LosePercentstr.set(1.0)
        self.txtLnum = tk.Entry(
            self, textvariable=self.LosePercentstr, font=f10, state=tk.DISABLED)
        self.btnLreset["relief"] = "sunken"

        self.btnWreset = tk.Button(                                             # 贏了後要做什麼的部分
            self, text="RESET TO BASE", font=f9, height=2, width=18, command=self.OnwinRB)
        self.WinPercentstr = tk.DoubleVar()
        self.WinPercentstr.set(0.0)

        self.btnWincrease = tk.Button(
            self, text="INCREASE BY", font=f9, height=2, width=18, command=self.OnwinIC)

        self.txtWnum = tk.Entry(
            self, textvariable=self.WinPercentstr, font=f10, state=tk.DISABLED)

        self.btnWreset["relief"] = "sunken"

       #---最底層ROLL,AUTO---#

        self.btnroll = tk.Button(
            self, text="ROLL", command=self.ROLL, font=f8, height=1, width=18, bg="ivory3")
        self.btnauto = tk.Button(
            self, text="Auto", font=f8, height=1, width=18, bg="ivory3", command=lambda: self.controller.show_roll())

        #++++++++++++++++++++++++++++++++++++#

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

    def written_payout(self, *args):
        try:
            self.WinChancestr.set(f"{99.0 / self.payoutstr.get():.2f}")
            self.ProfitOnWinstr.set(
                self.BetAmountstr.get() * (self.payoutstr.get() - 1))
        except:
            self.WinChancestr.set(0)
            self.ProfitOnWinstr.set(0)

    def written_bet(self, *args):
        try:
            self.ProfitOnWinstr.set(
                self.BetAmountstr.get() * (self.payoutstr.get() - 1))
            if self.BetAmountstr.get() >= self.moneystr.get():
                self.BetAmountstr.set(self.moneystr.get())
        except:
            self.ProfitOnWinstr.set(0)

    def written_money(self, *args):
        if self.moneystr.get() <= 0:
            Toplevel = tk.Toplevel()
            label = tk.Label(Toplevel, text="You are broken!!")
            button = tk.Button(Toplevel, text="Game Over",
                               command=self.controller.destroy)
            label.pack()
            button.pack()

    #+++++++++++++++++++++++++++++++++++++++++++++#

    def OnloseRB(self):
        self.txtLnum.config(state=tk.DISABLED)
        self.btnLreset["relief"] = "sunken"
        self.btnLincrease["relief"] = "raised"

    def OnloseIC(self):
        self.txtLnum.config(state=tk.NORMAL)
        self.btnLreset["relief"] = "raised"
        self.btnLincrease["relief"] = "sunken"

    def OnwinRB(self):
        self.txtWnum.config(state=tk.DISABLED)
        self.btnWreset["relief"] = "sunken"
        self.btnWincrease["relief"] = "raised"

    def OnwinIC(self):
        self.txtWnum.config(state=tk.NORMAL)
        self.btnWreset["relief"] = "raised"
        self.btnWincrease["relief"] = "sunken"

    #-----ROLL-----#

    def ROLL(self):
        rand = random.uniform(0, 100)

        money = self.moneystr.get()
        bet = self.BetAmountstr.get()
        win = self.WinChancestr.get()
        loseper = self.LosePercentstr.get()
        winper = self.WinPercentstr.get()
        payout = self.payoutstr.get()

        money -= bet
        profit = 0.0

        if rand <= win:
            money += bet * payout
            profit = bet * (payout - 1)
            if self.btnWreset["relief"] == "sunken":
                pass
            else:
                if winper != 0:
                    bet *= winper / 100

        else:
            profit = -bet
            if self.btnLreset["relief"] == "sunken":
                pass
            else:
                if loseper != 0:
                    bet *= loseper / 100

        if bet > money:
            bet = money

        self.moneystr.set(money)
        self.BetAmountstr.set(bet)
class Roll_Page(tk.Toplevel):

    def __init__(self, data):
        tk.Toplevel.__init__(self)
        self.createResultTitle(data)  # roll_page標題
        #self.createLabels()				# 存放執行結果的labels
        #self.get_data(data)				# 把StartPage選擇好的狀態抓下來
        #self.after(500, lambda: self.refresh(data))  # 重複更新
    def createResultTitle(self, data):
        f1 = tkfont.Font(size=10, family="Fixdsys", weight=tkfont.BOLD)

        self.ghost = tk.Label(self, text="", font=f1,
                              height=2, width=18)			# 下面都是標題宣告
        self.lbltime = tk.Label(self, text="Time", font=f1, height=2, width=18)
        self.lblbet = tk.Label(self, text="Bet", font=f1, height=2, width=18)
        self.lblmul = tk.Label(self, text="Multiplier",
                               font=f1, height=2, width=18)
        self.lblgame = tk.Label(self, text="Game", font=f1, height=2, width=18)
        self.lblroll = tk.Label(self, text="Roll", font=f1, height=2, width=18)
        self.lblprofit = tk.Label(
            self, text="Profit", font=f1, height=2, width=18)
        self.btnstop = tk.Button(self, text="Stop", font=f1,						# Stop按鈕，只有按了之後，money才會回傳
                                 height=2, width=18)
        self.lblani = tk.Label(self, text="randnum", font=f1, height=2, width=18)
        self.ghost.grid(row=0, column=0, sticky=tk.SW + tk.NE)
        self.lbltime.grid(row=1, column=0, sticky=tk.SW + tk.NE)
        self.lblbet.grid(row=1, column=1, sticky=tk.SW + tk.NE)
        self.lblmul.grid(row=1, column=2, sticky=tk.SW + tk.NE)
        self.lblgame.grid(row=1, column=3, sticky=tk.SW + tk.NE)
        self.lblroll.grid(row=1, column=4, sticky=tk.SW + tk.NE)
        self.lblprofit.grid(row=1, column=5, sticky=tk.SW + tk.NE)
        self.btnstop.grid(row=0, column=6, sticky=tk.SW + tk.NE)
        self.lblani.grid(row=0, column=7, sticky=tk.SW + tk.NE)
    #def show_roll(self):
    #    self.t = Roll_Page(self.frame)

if __name__ == "__main__":
    app = SampleApp()
    app.title("Gambling")
    app.mainloop()