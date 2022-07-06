import tkinter as tk
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld
from tktimepicker import constants

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

    print("Current Time =", hh, mm)
    print("Selected Time =", h, m)
    print("Result =", sec)

    seconds = now.timestamp()
    test = now.fromtimestamp(seconds)
    test2 = now.fromtimestamp(seconds + sec)
    print("Current time =", str(test).split(" ")[1])
    print("Calculated time", str(test2).split(" ")[1])

    return sec


def set_time():
    now = datetime.now()

    selected_hour = int(spin_hour.get())
    selected_min = int(spin_min.get())

    sec = get_sec_to_time(selected_hour, selected_min, int(now.strftime("%H")), int(now.strftime("%M")))

    os.system("shutdown -s -t " + str(sec))

def cancel_time():
    os.system("shutdown -a")

root = tk.Tk()

time = ()

time_lbl = tk.Label(root, text="Time:")
time_lbl.pack()

spin_hour = tk.Spinbox(root, increment=1, from_=0, to=23)
spin_hour.pack()

spin_min = tk.Spinbox(root, increment=1, from_=0, to=59)
spin_min.pack()

time_btn = tk.Button(root, text="Schedule shutdown", command=set_time)
time_btn.pack()

cancel_btn = tk.Button(root, text="Cancel shutdown", command=cancel_time)
cancel_btn.pack()

root.mainloop()