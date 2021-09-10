import tkinter as tk
import tkinter.messagebox as tmb
import pyautogui
import time
from tkinter import messagebox


root = tk.Tk()


# OptionMenu 7
tk.Label(root, text="SPAMしたいやつ").grid(row=1, sticky="e")
sv1 = tk.StringVar()
sv1.set('SPAM TOP')
tk.OptionMenu(root, sv1, 'Discord', 'Youtube', 'Minecraft', 'LINE').grid(row=1, column=1, padx=10, pady=10) 

def button_click():
  time.sleep(5)
  while True:
    pyautogui.write("aaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccc") # 文字入力
    pyautogui.press("enter") # エンター押すやつ
    time.sleep(0.1)

# Button 3
tk.Label(root, text="").grid(row=3, sticky="e")
tk.Button(root, text="実行",command=button_click).\
                grid(row=3, column=1, padx=10, pady=10)

# Message 11
tk.Label(root, text="").grid(row=5, sticky="e")
tk.Message(root, text="5秒後SPAMが始まるのでカーソル合わせろ").grid(row=5, column=1, padx=10, pady=10)

# Message 11
tk.Label(root, text="製作者:").grid(row=6, sticky="")
tk.Message(root, text="@Call56Call(@kinoko1216)").grid(row=6, column=1, padx=20, pady=20)


root.title("Simple Spammer!")
root.mainloop()
