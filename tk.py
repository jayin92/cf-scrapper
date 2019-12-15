# # 引入套件
# import tkinter as tk

# # 建立主視窗和 Frame（把元件變成群組的容器）
# window = tk.Tk()
# top_frame = tk.Frame(window)

# # 將元件分為 top/bottom 兩群並加入主視窗
# top_frame.pack()
# bottom_frame = tk.Frame(window)
# bottom_frame.pack(side=tk.BOTTOM)

# # 建立事件處理函式（event handler），透過元件 command 參數存取
# def echo_hello():
#     print('hello world :)')

# # 以下為 top 群組
# left_button = tk.Button(top_frame, text='Red', fg='red')
# # 讓系統自動擺放元件，預設為由上而下（靠左）
# left_button.pack(side=tk.LEFT)

# middle_button = tk.Button(top_frame, text='Green', fg='green')
# middle_button.pack(side=tk.LEFT)

# right_button = tk.Button(top_frame, text='Blue', fg='blue')
# right_button.pack(side=tk.LEFT)

# # 以下為 bottom 群組
# # bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
# bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_hello)
# # 讓系統自動擺放元件（靠下方）
# bottom_button.pack(side=tk.BOTTOM)

# # 運行主程式
# window.mainloop()

import tkinter as tk
import tkinter.font as tkFont
from get import get_info
from get import print_info

def search_b():
    handle = e.get()
    e.delete(0, 'end')

    if get_info(handle) != 0:
        re = get_info(handle)
        print_info(handle, re["rating"], re["rank"], re["maxRating"], re["maxRank"])

def search_e(event):
    handle = e.get()
    e.delete(0, 'end')
    if(len(handle) == 0):
        print("Please enter your handle.")
        return
    if get_info(handle) != 0:
        re = get_info(handle)
        print_info(handle, re["rating"], re["rank"], re["maxRating"], re["maxRank"])




window = tk.Tk()
ft_e = tkFont.Font(family="clean", size = 30)
ft_l = tkFont.Font(family="claen", size = 25)
window.title("Codeforces Scrapper")
# window.geometry("500x500")

username_lab = tk.Label(text="CF Handle", font=ft_l)
username_lab.pack(side=tk.LEFT, padx=10)
e = tk.Entry(window, font=ft_e)
e.focus()
window.bind("<Return>", search_e)
e.pack(side=tk.LEFT, padx=10)

search_b = tk.Button(window, text="Search", width=15, height=2, command=search_b)
search_b.pack(side=tk.LEFT, padx=10)

window.mainloop()