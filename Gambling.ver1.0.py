import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
import datetime

import random


class SampleApp(tk.Tk):
    # initialization

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default='Pixelpress-Pirates-Flag-Jolly-Roger.ico')
        # tk.Tk.wm_title(self, "Gambling")

        self.minsize(width=1100, height=700)
        self.maxsize(width=1100, height=700)

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
        self.betnow = 10.0

        self.lblBet = tk.Label(self, text="BET AMOUNT",
                               font=f3, height=2, width=49)
        self.txtDebt = tk.Entry(self, font=f4, textvariable=self.BetAmountstr)

        # BetAmount button 宣告
        self.btnhalf = tk.Button(
            self, text="1/2", command=lambda: self.BetAmountstr.set(self.BetAmountstr.get() / 2), font=f5, height=1, width=16)
        self.btndouble = tk.Button(
            self, text="x2", command=self.doublebet, font=f5, height=1, width=16)
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
            self, text="INCRASE BY(%)", font=f9, height=2, width=18, command=self.OnloseIC)

        self.LosePercentstr = tk.DoubleVar()
        self.LosePercentstr.set(100.0)
        self.txtLnum = tk.Entry(
            self, textvariable=self.LosePercentstr, font=f10, state=tk.DISABLED)
        self.btnLreset["relief"] = "sunken"

        self.btnWreset = tk.Button(                                             # 贏了後要做什麼的部分
            self, text="RESET TO BASE", font=f9, height=2, width=18, command=self.OnwinRB)
        self.WinPercentstr = tk.DoubleVar()
        self.WinPercentstr.set(100.0)

        self.btnWincrease = tk.Button(
            self, text="INCREASE BY(%)", font=f9, height=2, width=18, command=self.OnwinIC)

        self.txtWnum = tk.Entry(
            self, textvariable=self.WinPercentstr, font=f10, state=tk.DISABLED)

        self.btnWreset["relief"] = "sunken"

       #---最底層ROLL,AUTO---#

        self.btnroll = tk.Button(
            self, text="ROLL", command=self.ROLL, font=f8, height=1, width=18, bg="ivory3")
        self.btnauto = tk.Button(
            self, text="Auto", font=f8, height=1, width=18, bg="ivory3", command=lambda: self.controller.show_roll())

        #---roll時會顯示的東西---#

        self.lbltime = tk.Label(self, text="Time", font=f1, height=2, width=18)
        self.lblbet = tk.Label(self, text="Bet", font=f1, height=2, width=18)
        self.lblmul = tk.Label(self, text="Multiplier",
                               font=f1, height=2, width=18)
        self.lblgame = tk.Label(self, text="Game", font=f1, height=2, width=18)
        self.lblroll = tk.Label(self, text="Roll", font=f1, height=2, width=18)
        self.lblprofit = tk.Label(
            self, text="Profit", font=f1, height=2, width=18)

        self.lbltimeS = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lblbetS = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lblmulS = tk.Label(self, text="",
                               font=f1, height=2, width=18)
        self.lblgameS = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lblrollS = tk.Label(self, text="", font=f1, height=2, width=18)
        self.lblprofitS = tk.Label(
            self, text="", font=f1, height=2, width=18)

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
        self.lbltime.place(x=100, y=550)
        self.lblbet.place(x=250, y=550)
        self.lblmul.place(x=400, y=550)
        self.lblgame.place(x=550, y=550)
        self.lblroll.place(x=700, y=550)
        self.lblprofit.place(x=850, y=550)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lbltimeS.place(x=100, y=580)
        self.lblbetS.place(x=250, y=580)
        self.lblmulS.place(x=400, y=580)
        self.lblgameS.place(x=550, y=580)
        self.lblrollS.place(x=700, y=580)
        self.lblprofitS.place(x=850, y=580)
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
            self.betnow = self.BetAmountstr.get()
            self.ProfitOnWinstr.set(
                self.BetAmountstr.get() * (self.payoutstr.get() - 1))
            if self.BetAmountstr.get() >= self.moneystr.get():
                self.BetAmountstr.set(self.moneystr.get())
        except:
            self.ProfitOnWinstr.set(0)

    def written_money(self, *args):
        f1 = tkfont.Font(size=120, family="Fixdsys", weight=tkfont.BOLD)
        f2 = tkfont.Font(size=70, family="Fixdsys", weight=tkfont.BOLD)
        if self.moneystr.get() <= 0:
            Toplevel = tk.Toplevel()
            label = tk.Label(Toplevel, text="You are broken!!", font=f1, bg="red")
            button = tk.Button(Toplevel, text="Game Over",
                               command=self.controller.destroy, font=f2, fg="red", bg='ivory3')
            label.pack()
            button.pack()

    def doublebet(self):
        if self.BetAmountstr.get() > self.moneystr.get() / 2:
            self.BetAmountstr.set(self.moneystr.get())
        else:
            self.BetAmountstr.set(self.BetAmountstr.get() * 2)



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
        self.lbltimeS["text"] = datetime.datetime.now().strftime("%H:%M:%S")
        self.lblbetS["text"] = str(bet)
        self.lblmulS["text"] = str(self.payoutstr.get())
        self.lblgameS["text"] = "<" + str(self.WinChancestr.get())
        self.lblrollS["text"] = str(round(rand, 2))

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


        self.lblprofitS["text"] = str(profit)

        self.moneystr.set(money)
        self.BetAmountstr.set(bet)


# 執行結果在這個頁面顯示


class Roll_Page(tk.Toplevel):

    def __init__(self, data):
        tk.Toplevel.__init__(self)
        self.createResultTitle(data)  # roll_page標題
        self.createLabels()				# 存放執行結果的labels
        self.get_data(data)				# 把StartPage選擇好的狀態抓下來
        self.after(500, lambda: self.refresh(data))  # 重複更新

    def get_data(self, data):
        self.money = data.moneystr.get()		          					# 使用者持有金錢
        self.originbet = self.bet = data.BetAmountstr.get()	            	# 使用者的賭金
        self.rollnum = data.WinChancestr.get()			                   	# 目標數字
        self.payout = data.payoutstr.get()					             	# 賠率
        if data.btnLreset["relief"] == "sunken":					       	# 檢測使用者有沒有選擇retrurn to base
            self.LRB = True
        else:
            self.LRB = False
            self.LIC = data.LosePercentstr.get() / 100
        if data.btnWreset["relief"] == "sunken":
            self.WRB = True
        else:
            self.WRB = False
            self.WIC = data.WinPercentstr.get() / 100

    def createResultTitle(self, data):
        f1 = tkfont.Font(size=13, family="Fixdsys", weight=tkfont.BOLD)

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
        self.destroy()

    def createLabels(self):															# 宣告存放執行結果的labels,放在二維list裡
        f1 = tkfont.Font(size=14, family="Fixdsys", weight=tkfont.BOLD)
        self.labels = [[tk.Label(self, text="", font=f1, height=2, width=18)
                        for j in range(6)] for i in range(7)]
        for i in range(7):
            for j in range(6):
                self.labels[i][j].grid(
                    row=i + 2, column=j, sticky=tk.SW + tk.NE)

    def refresh(self, data):																# 更新資料函式宣告
        for i in range(6, 0, -1):													# 首先把每一行的資料都平行向下一格
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

        data.moneystr.set(str(self.money))											# 把money資料回傳
        if self.money > 0:
            self.after(500, lambda: self.refresh(data))


if __name__ == "__main__":
    app = SampleApp()
    app.title("Gambling")
    app.mainloop()
