###目前狀況###

#2018.12.27
#可以更改除了Manual和Auto以外所有可控的面板數字或模式
#透過輸入(可控)後面的("xxx")來更改
#輸入"END"結束遊戲
#注額預設14
#OnLosePercent預設0.87
#money低於MinBet時遊戲自動結束

#2018.12.25
#先輸入username
#輸入 "a" 就會roll一次
#輸入 "b" 就會直接結束遊戲
#資產預設100
#注額預設20
#勝率預設49.5
#賠率預設2
#輸錢時賭資加倍
#money為0時遊戲自動結束

###目前狀況###



###函數名稱介紹###

#username 玩家名稱(輸入)
#money 目前資產(預設100)
#Number 轉出的數字(預設0))

#BetAmount 原始下注金額(可控)("ba")(預設20)
#BetHalf 改下一半 ("bh")
#BetDouble 改下2倍 ("bd")
#BetMax 全押 ("bm")

#BetNow 目前下注金額

#ProfitOnWin 獲勝獎金-本金
#MaxBet 最高下注金額(設10000000.00)
#MinBet 最低下注金額(設0.00000001)

#RollUnderToWin
#WinChance % 獲勝機率(可控)("wc")(預設49.5)
#Payout 賠率(可控)("p")(預設2)
#勝率 * 賠率 = 99

#LoseType 輸時改注模式(可控)("lt")(預設IB)("A" : reset to base,"B" : increase by)
#OnLosePercent 增加% (可控)("lp")

#WinType 贏時改注模式(可控)("wt")(預設RTB)("A" : reset to base,"B" : increase by)
#OnWinPercent 增加%(可控)("wp")

#RollType 拉霸模式(可控)(預設Manual)("A" : Manual,"B" : Auto)



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
	
	

###輸入玩家名稱###
	
print("username")
username = str(input())



###預設各項參數###

money = float(100)
Number = float(0)

BetAmount = float(14.0) #更改 : "ba"
BetNow = BetAmount

Payout = float(2.0) #更改 : "p"
WinChance = float(99.0/Payout) #更改 : "wc"
RollUnderToWin = WinChance

ProfitOnWin = profit(BetAmount,Payout)
MaxBet = float(10000000)
MinBet = float(0.00000001)

LoseType = "B" #更改 : "lt"
OnLosePercent = float(0.87) #更改 : "lp"

WinType = "A" #更改 : "wt"
OnWinPercent = float(0) #更改 : "wp"



###正式開始操作###

while True :

	x = input() #輸入"a" = Roll

	if x == "a" and money > MinBet :

		
		#先從資產扣除本次注額
		money -= BetNow
			
		#隨機轉出數字
		Number = RandomRoll(Number)

		if Number <= RollUnderToWin :
		
			#若轉出的數字小於設定,則總資產增加(注額*賠率)
			money += BetNow * Payout
		
			if WinType == "A" :

				#若贏時加注模式為RTB,則下注金額回復原先設定
				BetNow = BetAmount
				
			elif WinType == "B" :
				
				#下次賭金自動增加設定%數
				BetNow = IncreaseBy(BetNow,OnWinPercent) 

		else :
		
			#輸錢不退還注額
		
			if LoseType == "A" :
			
				#若輸時加註模式為RTB,則下注金額恢復原先設定
				BetNow = BetAmount
				
			elif LoseType == "B" :
				
				#下次賭金自動增加設定%數
				BetNow = IncreaseBy(BetNow,OnLosePercent)
				
		
		if money < BetNow :
		
			BetAmount = money
			BetNow = money
			ProfitOnWin = profit(BetAmount,Payout)
		
	
	elif x == "END" :
		
		#結束遊戲
	
		print("END")
		break
	
	
	elif x == "ba" :
		
		#重新設定注額,超過資產或投注上限時自動改成資產或上限
		#低於最小注額時自動改成MinBet
		
		BetAmount = float(input())
		
		if BetAmount > money :
			
			BetAmount = money
			
		elif BetAmount > MaxBet :
			BetAmount = MaxBet
		
		elif BetAmount < MinBet :
			
			BetAmount = MinBet

		BetNow = BetAmount
		ProfitOnWin = profit(BetAmount,Payout)
		
	
	
	elif x == "p" :

		#重設賠率,勝率自動調整
		Payout = float(input())
		WinChance = float(99.0/Payout)
		RollUnderToWin = WinChance
		ProfitOnWin = profit(BetAmount,Payout)
		
	elif x == "wc" :
	
		#重設勝率,賠率自動調整
		WinChance = float(input())
		Payout = float(99.0/WinChance)	
		RollUnderToWin = WinChance
		ProfitOnWin = profit(BetAmount,Payout)
		
	elif x == "lt" :
		
		#重設LoseType,("A" : RTB , "B" : IB)
		LoseType = str(input())
		
		
	elif x == "lp" :

		#重設OnLosePercent
		OnLosePercent = float(input())
	
	
	elif x == "wt" :
	
		#重設WinType,("A" : RTB , "B" : IB)
		WinType = str(input())
	
	
	elif x == "wp" :
		
		#重設OnWinPercent
		OnWinPercent = float(input())
	
	
	elif x == "bh" :
	
		#改下一半
		BetAmount = BetHalf(BetAmount)
	
		if BetAmount < MinBet :
			BetAmount = MinBet
			
		BetNow = BetAmount
		ProfitOnWin = profit(BetAmount,Payout)
		
		
	elif x == "bd" :
	
		#改下兩倍
		BetAmount = BetDouble(BetAmount)
	
		if BetAmount > money :
			BetAmount = money
			
		elif BetAmount > MaxBet :
			BetAmount = MaxBet
			
		BetNow = BetAmount
		ProfitOnWin = profit(BetAmount,Payout)
		
		
	elif x == "bm" :
		
		#全押
		BetAmount = BetMax(BetAmount)
		BetNow = BetAmount
		ProfitOnWin = profit(BetAmount,Payout)
	
	
	else :
	
		pass
	
	
	
	#玩家名稱,總資產
	print(username,money)
	#設定注額,獲勝利潤
	print(BetAmount,ProfitOnWin)
	#贏錢數字,賠率,勝率
	print(RollUnderToWin,Payout,WinChance)
	#贏/輸時加注模式
	if WinType == "A" :
		print("RESET TO BASE",end = ",")
	else :
		print("INCREASE BY",end = ",")
	if LoseType == "A" :
		print("RESET TO BASE")
	else :
		print("INCREASE BY")	
	#本次轉出數字
	print(Number)
	print(BetNow)
	
		
	if money <= MinBet :
		
		print("END")
		break