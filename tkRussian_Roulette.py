import tkinter as tk
import random as rd
import os


class View(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.winfo_toplevel().title("Russian Roulette")
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.text = tk.Label(self)
        self.text["text"] = "Click Button to check your fortune!"
        self.text["width"] = "60"
        self.text["height"] = "5"
        self.text.grid(row = 0,
                       column = 0, 
                       sticky = tk.N)
        self.status_text = tk.Label(self)
        self.status_text["text"] = ""
        self.status_text.grid(row = 1,
                              column = 0, 
                              sticky = tk.N)
        self.button = tk.Button(self)
        self.button["text"] = "Button"
        self.button.grid(row = 2,
                         column = 0, 
                         pady=30, 
                         sticky = tk.N)


class Logic:
    def shutdown(self):
        return 1 if rd.random() < rd.random() else 0


class Controller:
    def __init__(self):
        self.gun = Logic()

        self.app = View(master = tk.Tk())
        self.app.button["command"] = self.start
        self.app.mainloop()
      
    def start(self):
        if self.gun.shutdown():
            self.app.status_text["text"] = "You got a shot!"
            os.system("shutdown -s -t 3")
        else:
            self.app.status_text["text"] = "You have a lucky escape!"


if __name__ == "__main__":
    app = Controller()