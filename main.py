import tkinter as tk
import os
from datetime import datetime 

def get_sec_to_time(h, m, hh, mm):
    now = datetime.now()
        
    sec = 0
    if h < hh:
        sec = get_sec_to_time(24, 00, hh, mm) + get_sec_to_time(h, m, 0, 0)
    else:
        dh = h-hh
        dm = m-mm
        sec = abs(dh*3600+dm*60)

    #print("Current Time =", hh, mm)
    #print("Selected Time =", h, m)
    #print("Result =", sec)

    seconds = now.timestamp()
    test = now.fromtimestamp(seconds)
    test2 = now.fromtimestamp(seconds + sec)
    #print("Current time =", str(test).split(" ")[1])
    #print("Calculated time", str(test2).split(" ")[1])

    return sec


def set_time():
    now = datetime.now()

    selected_hour = int(spin_hour.get())
    selected_min = int(spin_min.get())

    sec = get_sec_to_time(selected_hour, selected_min, int(now.strftime("%H")), int(now.strftime("%M")))

    os.system("shutdown -s -t " + str(sec))

def cancel_time():
    os.system("shutdown -a")

def cicle_hours():
    selected_hour = int(spin_hour.get())
    if selected_hour < 0:
        hour.set(23)
    elif selected_hour > 23:
        hour.set(0)

def cicle_min():
    selected_min = int(spin_min.get())
    if selected_min < 0:
        min.set(59)
    elif selected_min > 59:
        min.set(0)
        

root = tk.Tk()
root.resizable(False, False)
root.title("SD Scheduler")
root.iconbitmap("icon.ico")
frm = tk.Frame(root)
frm.grid()

_now = datetime.now()

hour = tk.StringVar(root)
hour.set(_now.strftime("%H"))
spin_hour = tk.Spinbox(frm, increment=1, from_=-1, to=24, textvariable=hour, command=cicle_hours)
spin_hour.grid(column=0, row=0)

min = tk.StringVar(root)
min.set(_now.strftime("%M"))
spin_min = tk.Spinbox(frm, increment=1, from_=-1, to=60, textvariable=min, command=cicle_min)
spin_min.grid(column=1, row=0)

time_btn = tk.Button(frm, text="Schedule shutdown", command=set_time).grid(column=0, row=1)

cancel_btn = tk.Button(frm, text="Cancel shutdown", command=cancel_time).grid(column=1, row=1)

root.mainloop()