import csv
import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from PIL import Image, ImageTk

import random

def RandomRoll(number) :
    out = random.uniform(0,100)
    return out

def profit(BetAmount,Payout) :
    ProfitOnWin = (BetAmount*Payout) - BetAmount
    return ProfitOnWin


    
money = float(100)
Number = float(0)

BetAmount = float(10.0)
BetNow = BetAmount

Payout = float(2.0) 
WinChance = float(99.0/Payout)
RollUnderToWin = WinChance

ProfitOnWin = profit(BetAmount,Payout)


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
        self.btn1 = ttk.Button(self, text="Start Game", width=15,command=lambda: controller.show_roll())
        self.btn1.place(x=520, y=550)
    
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
  
        self.lblname = tk.Label(self, text="Username",font=f1, height=1, width=15)
        self.lblmoney = tk.Label(self, text="Money", font=f1, height=1, width=15)
        
        self.moneystr = tk.StringVar()
        self.moneystr.set(str(money))
        self.Mymoney = tk.Label(self,textvariable = self.moneystr, font=f2)
        
        self.username = tk.Entry(self, font=f2) 
              
              
              
       #---第二層(BetAmount,ProfitOnWin)---#
        
        # BetAmount 宣告
        self.BetAmountstr = tk.StringVar()
        self.BetAmountstr.set("10.0")
        
        self.lblBet = tk.Label(self, text="BET AMOUNT",font=f3, height=2, width=49)
        self.txtDebt = tk.Entry(self, font=f4,textvariable = self.BetAmountstr)
        
        BetAmount = float(self.BetAmountstr.get())
        
        # BetAmount button 宣告
        self.btnhalf = tk.Button(self, text="1/2", command = self.BetHalf, font=f5, height=1, width=16)
        self.btndouble = tk.Button(self, text="x2", command = self.BetDouble, font=f5, height=1, width=16)
        self.btnmax = tk.Button(self, text="MAX", command = self.BetMax, font=f5, height=1, width=15)
  

       #---第三層(PAYOUT,RollUnderToWin,WinChance)---#
  
        self.payoutstr = tk.StringVar()
        self.payoutstr.set("2.0")
       
        self.lblPay = tk.Label(self, text="PAYOUT",height=3, width=20, font=f6)
        self.txtpayout = tk.Entry(self, font=f7, textvariable = self.payoutstr)
              
        Payout = float(self.txtpayout.get())
 
        WinChance = float(99/Payout)
        
        self.WinChancestr = tk.StringVar()
        self.WinChancestr.set(str(WinChance))
        
        self.lblUnderwin = tk.Label(self, text="ROLL UNDER TO WIN", height=3, width=20, font=f6)
        self.lblundernum = tk.Label(self, font=f7,textvariable = self.WinChancestr)
                
        self.lblChance = tk.Label(self, text = 'WIN CHANCE%',font=f6, height=3, width=30)
        self.lblchange = tk.Label(self, textvariable = self.WinChancestr, height=2, width=30, font=f6)
                
        
       #---第二層ProfitOnWin---#
        
        self.ProfitOnWinstr = tk.StringVar()
        self.ProfitOnWinstr.set(str(BetAmount*(Payout-1)))
        
        self.lblProfit = tk.Label(self, text="PROFIT ON WIN", font=f5, height=2, width=50)          
        self.Profit = tk.Label(self, textvariable = self.ProfitOnWinstr, font=f3, height=2, width=50, bg='white')

        
       #---第四層(ONWIN,ONLOSE)---#

        self.lblLose = tk.Label(self, text="ON LOSE",font=f9, height=3, width=35)
        self.lblWin = tk.Label(self, text="ON WIN",font=f9, height=3, width=35)
        self.btnLreset = tk.Button(self, text="RESET TO BASE", font=f9, height=2, width=18)
        self.btnLincrease = tk.Button(self, text="INCRASE BY", font=f9, height=2, width=18)
        self.txtLnum = tk.Entry(self, font = f10)
        self.btnWreset = tk.Button(self, text="RESET TO BASE", font=f9, height=2, width=18)
        self.btnWincrease = tk.Button(self, text="INCREASE BY", font=f9, height=2, width=18)
        self.txtWnum = tk.Entry(self, font = f10)
        
        
       #---BetNow設定---#
       
        
        
       #---最底層ROLL,AUTO---#
        
        
        self.btnroll = tk.Button(self, text="ROLL",command = self.ROLL,font=f8, height=1, width=18, bg="ivory3")
        self.btnauto = tk.Button(self, text="Auto", font=f8, height=1, width=18, bg="ivory3")

       
       
       
       
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblname.place(x=100, y=10)
        self.lblmoney.place(x = 300, y = 10)
        self.username.place(x = 200, y = 10, width = 75)
        self.Mymoney.place(x = 400, y = 10, width = 300)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblBet.place(x = 100, y = 60)
        self.lblProfit.place(x = 600, y = 60)
        self.txtDebt.place(x = 100, y = 100)
        self.Profit.place(x = 600, y = 100)
        self.btnhalf.place(x = 100, y = 150)
        self.btndouble.place(x = 253, y = 150)
        self.btnmax.place(x = 406, y = 150)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblUnderwin.place(x = 100, y = 200)
        self.lblundernum.place(x = 100, y = 250, width=185)
        self.lblPay.place(x = 500, y = 200)
        self.txtpayout.place(x = 500, y = 250, width=185)
        self.lblChance.place(x = 800, y = 200)
        self.lblchange.place(x = 800, y = 250)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.lblLose.place(x = 160, y = 320)
        self.lblWin.place(x = 660, y = 320)
        self.btnLreset.place(x = 100, y = 370)
        self.btnLincrease.place(x = 253, y = 370)
        self.txtLnum.place(x = 415, y = 370, width=100)
        self.btnWreset.place(x = 600, y = 370)
        self.btnWincrease.place(x = 753, y = 370)
        self.txtWnum.place(x = 905, y = 370, width=100)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
        self.btnroll.place(x = 200, y = 450)
        self.btnauto.place(x = 600, y = 450)
        #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#   
        
        
        
    # 所有button函式
    def BetHalf(self):
        
        global BetAmount
        global BetNow
        
        self.BetAmountstr.set(str(BetAmount*0.5))
        BetAmount *= 0.5
        BetNow = BetAmount
        ProfitOnWin = profit(BetAmount,Payout)
        self.ProfitOnWinstr.set(str(ProfitOnWin))
        
    def BetDouble(self):
        
        global BetAmount
        global BetNow
        
        if (BetAmount*2 > money) :
            self.BetAmountstr.set(str(money))
            BetAmount = money
            BetNow = BetAmount
            ProfitOnWin = profit(BetAmount,Payout)
            self.ProfitOnWinstr.set(str(ProfitOnWin))
        else :
            self.BetAmountstr.set(str(BetAmount*2))
            BetAmount *= 2
            BetNow = BetAmount
            ProfitOnWin = profit(BetAmount,Payout)
            self.ProfitOnWinstr.set(str(ProfitOnWin))
            
    def BetMax(self):
    
        global BetAmount
        global BetNow
    
        self.BetAmountstr.set(str(money))
        BetAmount = money
        BetNow = BetAmount
        ProfitOnWin = profit(BetAmount,Payout)
        self.ProfitOnWinstr.set(str(ProfitOnWin))
    
    #-----ROLL-----#
    
    def ROLL(self) :
    
        global money
        global BetAmount
        
        BetAmount = float(self.txtDebt.get())
        Payout = float(self.txtpayout.get())
        BetNow = BetAmount
        
        WinChance = float(99/Payout)
        self.WinChancestr.set(str(WinChance))
        
        self.ProfitOnWinstr.set(str(BetAmount*(Payout-1)))
       
        if BetNow <= money : 
        
            money -= BetNow
            RollNumber = random.uniform(0,100)
       
            print(RollNumber)
       
            if RollNumber < 49.5 :
            
                money += BetNow*Payout
                self.moneystr.set(str(money))
                        
            else :
           
                self.moneystr.set(str(money))
        
# 執行結果在這個頁面顯示
    
class Roll_Page(tk.Toplevel):
    def __init__(self, data):
        tk.Toplevel.__init__(self)
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

        self.ghost.grid(row=0, column=0, sticky=tk.SW + tk.NE)
        self.lbltime.grid(row=1, column=0, sticky=tk.SW + tk.NE)
        self.lblbet.grid(row=1, column=1, sticky=tk.SW + tk.NE)
        self.lblmul.grid(row=1, column=2, sticky=tk.SW + tk.NE)
        self.lblgame.grid(row=1, column=3, sticky=tk.SW + tk.NE)
        self.lblroll.grid(row=1, column=4, sticky=tk.SW + tk.NE)
        self.lblprofit.grid(row=1, column=5, sticky=tk.SW + tk.NE)

if True:
    app = SampleApp()
    app.title("Gambling")
    app.mainloop()