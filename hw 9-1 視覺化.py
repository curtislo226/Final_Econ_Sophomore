import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class Calculator(tk.Frame):
  
  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()
    
  def createWidgets(self):
    f1 = tkFont.Font(size = 38, family = "Fixdsys", weight=tkFont.BOLD)
    f2 = tkFont.Font(size = 20, family = "Fixdsys", weight=tkFont.BOLD)
	
    self.txtnum = tk.Text(self, height = 1, width = 10, font = f1) #製造一個文字框
    self.dropdown = ttk.Combobox(self, width = 15)  #製造一個下拉選單
    self.dropdown['values'] = ("平方", "立方")      #選項有平方跟立方
    self.button = tk.Button(self, text = "run", command = self.clickbutton, height = 1, width = 3, font = f2)
    #製造一個運算按鈕
  
    self.txtnum.grid(row = 0, column = 0, columnspan = 2)
    self.dropdown.grid(row = 1, column = 0)
    self.button.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)

  def clickbutton(self):       #按下button後，下拉選單選擇甚麼對數字進行該計算
    curNum = float(self.txtnum.get("1.0", tk.END))  #先把目前文字框輸入的數字存取起來
    self.txtnum.delete("1.0", tk.END)               #將文字框裡面數字刪除
    if self.dropdown.get() == "平方":               #若下拉選單選擇"平方"則數字平方
        self.txtnum.insert("1.0", str(curNum ** 2))
    elif self.dropdown.get() == "立方":             #若下拉選單選擇"立方"則數字立方
        self.txtnum.insert("1.0", str(curNum ** 3))
        
cal = Calculator()
cal.master.title("My HW9-1")
cal.mainloop()
