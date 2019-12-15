import tkinter as tk
import tkinter.font as tkFont
from get import get_info
from get import print_info

window = tk.Tk()
window.title("Codeforces Scrapper")
ft_e = tkFont.Font(size = 30)
ft_l = tkFont.Font(size = 25)

def search_b():
    handle = e.get()
    e.delete(0, 'end')
    if(len(handle) == 0):
        info_lab.configure(text = "Please enter your handle.")
        return
    if get_info(handle) != 0:
        re = get_info(handle)
        try:
            info_lab.configure(text = print_info(handle, re["rating"], re["rank"], re["maxRating"], re["maxRank"]))
        except:
            info_lab.configure(text = print_info(handle))
    else:
        info_lab.configure(text = "User Not Found")
def search_e(event):
    handle = e.get()
    e.delete(0, 'end')
    if(len(handle) == 0):
        info_lab.configure(text = "Please enter your handle.")
        return
    if get_info(handle) != 0:
        re = get_info(handle)
        try:
            info_lab.configure(text = print_info(handle, re["rating"], re["rank"], re["maxRating"], re["maxRank"]))
        except:
            info_lab.configure(text = print_info(handle))
    else:
        info_lab.configure(text = "User Not Found")



# window.geometry("500x500")

username_lab = tk.Label(text="CF Handle", font=ft_l)
username_lab.pack(side=tk.LEFT, padx=10)
e = tk.Entry(window, font=ft_e)
e.focus()
window.bind("<Return>", search_e)
e.pack(side=tk.LEFT, padx=10)

search_b = tk.Button(window, text="Search", width=15, height=2, command=search_b)
search_b.pack(side=tk.LEFT)

info_lab = tk.Label(text="", font=ft_l, justify=tk.LEFT, anchor='w')
info_lab.pack(padx=10)
window.mainloop()