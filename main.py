from tabnanny import check
import tkinter as tk
import os
from datetime import datetime 

def get_sec_to_time(h, m, hh, mm):
    sec = 0
    if h < hh:
        sec = get_sec_to_time(24, 00, hh, mm) + get_sec_to_time(h, m, 0, 0)
    else:
        dh = h-hh
        dm = m-mm
        sec = abs(dh*3600+dm*60)

    return sec

def calc_sec_to_time(sec):
    h=sec//3600
    m=(sec%3600)//60
    return h, m

def sum_time_to_current_time(h, m):
    now = datetime.now()

    ch = int(now.strftime("%H"))
    cm = int(now.strftime("%M"))

    res_h = ch + h

    mm = cm + m
    res_m = mm
    if mm > 59:
        res_h += 1
        res_m = mm - 60

    return res_h, res_m

def set_time():
    now = datetime.now()

    selected_hour = int(spin_hour.get())
    selected_min = int(spin_min.get())

    sec = get_sec_to_time(selected_hour, selected_min, int(now.strftime("%H")), int(now.strftime("%M")))

    os.system("shutdown -s -t " + str(sec))

def cancel_time():
    os.system("shutdown -a")

def cicle_hours():
    check_0_val.set(True)
    check_1_val.set(False)
    cicle_input(hour, spin_hour.get(), 0, 23)

def cicle_min():
    check_0_val.set(True)
    check_1_val.set(False)
    cicle_input(min, spin_min.get(), 0, 59)

def cicle_hours_disc():
    check_0_val.set(False)
    check_1_val.set(True)
    cicle_input(hour_disc, spin_hour_disc.get(), 0, 23)

def cicle_min_disc():
    check_0_val.set(False)
    check_1_val.set(True)
    cicle_input(min_disc, spin_min_disc.get(), 0, 59)

def cicle_input(var, val, min, max):
    val = int(val)
    if val > max:
        var.set(min)
    elif val < min:
        var.set(max)

def check_0_trigger():
    if not check_0_val.get():
        check_0_val.set(True)
        return
    check_1_val.set(False)

def check_1_trigger():
    if not check_1_val.get():
        check_1_val.set(True)
        return
    check_0_val.set(False)

def update_time():
    if check_0_val.get():
        update_countdown()
    else:
        update_normal_time()
    root.after(1000, update_time)

def update_normal_time():
    selected_hour_disc = int(spin_hour_disc.get())
    selected_min_disc = int(spin_min_disc.get())

    h, m = sum_time_to_current_time(selected_hour_disc, selected_min_disc)
    
    hour.set(h)
    min.set(m)

def update_countdown():
    now = datetime.now()

    selected_hour = int(spin_hour.get())
    selected_min = int(spin_min.get())

    sec = get_sec_to_time(selected_hour, selected_min, int(now.strftime("%H")), int(now.strftime("%M")))

    h, m = calc_sec_to_time(sec)

    hour_disc.set(h)
    min_disc.set(m)
    

root = tk.Tk()
root.resizable(False, False)
root.title("SD Scheduler")
root.iconbitmap("icon.ico")
frm = tk.Frame(root)
frm.grid()

_now = datetime.now()

check_0_val = tk.BooleanVar(root)
check_0_val.set(True)
check_0 = tk.Checkbutton(frm, text="Exact time", variable=check_0_val, command=check_0_trigger)
check_0.grid(column=0, row=0, sticky="W")

hour = tk.StringVar(root)
hour.set(_now.strftime("%H"))
spin_hour = tk.Spinbox(frm, increment=1, from_=-1, to=24, textvariable=hour, command=cicle_hours)
spin_hour.grid(column=0, row=1)

min = tk.StringVar(root)
min.set(_now.strftime("%M"))
spin_min = tk.Spinbox(frm, increment=1, from_=-1, to=60, textvariable=min, command=cicle_min)
spin_min.grid(column=1, row=1)

check_1_val = tk.BooleanVar(root)
check_1 = tk.Checkbutton(frm, text="Count down", variable=check_1_val, command=check_1_trigger)
check_1.grid(column=0, row=2, sticky="W")

hour_disc = tk.StringVar(root)
hour_disc.set(_now.strftime("%H"))
spin_hour_disc = tk.Spinbox(frm, increment=1, from_=-1, to=24, textvariable=hour_disc, command=cicle_hours_disc)
spin_hour_disc.grid(column=0, row=3)

min_disc = tk.StringVar(root)
min_disc.set(_now.strftime("%M"))
spin_min_disc = tk.Spinbox(frm, increment=1, from_=-1, to=60, textvariable=min_disc, command=cicle_min_disc)
spin_min_disc.grid(column=1, row=3)

time_btn = tk.Button(frm, text="Schedule shutdown", command=set_time).grid(column=0, row=4)

cancel_btn = tk.Button(frm, text="Cancel shutdown", command=cancel_time).grid(column=1, row=4)

update_time()
root.mainloop()