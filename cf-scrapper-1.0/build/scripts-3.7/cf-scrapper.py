#!python

import tkinter as tk
import tkinter.font as tkFont
import requests
import json
import sys 
from math import ceil, floor
base_url = "https://codeforces.com/api/user.info?handles="

def print_info(handle_, rating = "0", rank = "EMPTY", max_rating = "0", max_rank = "EMPTY"):
    max_len = max(len((handle_)), len(str(rating)), len(rank), len(str(max_rating)), len(max_rank))
    max_len += 17 - 6

    info = ""
    info += '-'* floor(max_len / 2) +" INFO " + '-'* ceil(max_len / 2) + '\n'
    info += "Handle         : " + handle_ + '\n'
    info += "Current rating : " + str(rating) + '\n'
    info += "Current rank   : " + rank + '\n'
    info += "Max rating     : " + str(max_rating) + '\n'
    info += "Max rank       : " + max_rank + '\n'
    info += "-" * (max_len+6)
    return info

def get_info(handle_):
    r = requests.get(base_url+handle_)

    if r.json()["status"] == "FAILED":
        return 0
    
    return r.json()["result"][0]


window = tk.Tk()
window.title("Codeforces Scrapper")
window.iconbitmap("favicon.ico")
ft_e = tkFont.Font(family = "Consolas", size = 30)
ft_l = tkFont.Font(family = "Consolas", size = 25)

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
