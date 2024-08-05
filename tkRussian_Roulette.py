import tkinter as tk
import random as rd
import os

# View類別
class View(tk.Frame):
    # 設定初始值
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.winfo_toplevel().title("俄羅斯輪盤")
        self.grid()
        self.createWidgets()
        
    # 建立視窗元件
    def createWidgets(self):
        # 說明
        self.text = tk.Label(self)
        self.text["text"] = "點擊按鈕，試試你的運氣！"
        self.text["width"] = "60"
        self.text["height"] = "5"
        self.text.grid(row = 0,
                       column = 0, 
                       sticky = tk.N)
        # 狀態
        self.status_text = tk.Label(self)
        self.status_text["text"] = ""
        self.status_text.grid(row = 1,
                              column = 0, 
                              sticky = tk.N)
        # 按鈕
        self.button = tk.Button(self)
        self.button["text"] = "按鈕"
        self.button.grid(row = 2,
                         column = 0, 
                         pady=30, 
                         sticky = tk.N)
# 主邏輯
class Logic:
    def shutdown(self):
        # return "中槍了！" if rd.random() < rd.random() else "幸運逃過一劫！"
        return 1 if rd.random() < rd.random() else 0
# GUI類別，整合
class Controller:
    #設定初始值
    def __init__(self):
        self.gun = Logic()

        self.app = View(master = tk.Tk())
        self.app.button["command"] = self.start
        self.app.mainloop()
      
    #按下【按鈕】按鈕的事件
    def start(self):
        if self.gun.shutdown():
            # print("中槍了！")
            self.app.status_text["text"] = "中槍了！"
            # os.system("shutdown -s -t 3")
        else:
            # print("幸運逃過一劫！")
            self.app.status_text["text"] = "幸運逃過一劫！"

if __name__ == "__main__":
    # root = tk.Tk()
    # app = View(master = root)
    # root.mainloop()

    # lg = Logic()
    # print(lg.shutdown())

    app = Controller()