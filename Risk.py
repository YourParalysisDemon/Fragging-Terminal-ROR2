import keyboard
import tkinter as tk
import webbrowser
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from subprocess import Popen
# Add this cause felt like it
while True:
    password = input("Enter password ")
    if password == "111":  # Is the best password in world!!!
        print("Welcome")
        break
    else:  # lol
        print("Try again retard")

mem = Pymem("Risk of Rain 2.exe")
module = module_from_name(mem.process_handle, "UnityPlayer.dll").lpBaseOfDll
health_offsets = [0X8, 0X10, 0X30, 0X108, 0X28, 0X68]
fire_offsets = [0X8, 0X10, 0X30, 0XA8, 0X28, 0X80]
ice_offsets = [0X8, 0X10, 0X30, 0XC8, 0X28, 0X80]
ball_offsets = [0X0, 0X10, 0X30, 0XC8, 0X110, 0X28, 0X120]


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def multi_run_god():
    new_thread = Thread(target=god_mode, daemon=True)
    new_thread.start()


def god_mode():
    addr1 = getpointeraddress(module + 0x017FBCE8, health_offsets)
    addr2 = getpointeraddress(module + 0x017FBCE8, fire_offsets)
    addr3 = getpointeraddress(module + 0x017FBCE8, ice_offsets)
    addr4 = getpointeraddress(module + 0x017FBCE8, ball_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x460ca000)
            mem.write_int(addr2, 0x00000fa3)
            mem.write_int(addr3, 0x00000fa3)
            mem.write_int(addr4, 0x00000fa3)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def kill_hack():
    addr = getpointeraddress(module + 0x017FBCE8, health_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def open_msn():
    webbrowser.open_new("C:/Microsoft/Windows")


def open_calc():
    Popen("calc.exe")


def open_paint():
    Popen("mspaint.exe")


root = tk.Tk()
root.title("Fragging Terminal")
root.geometry("260x320")
root.configure(background='black')
root.attributes("-topmost", True)


def show():
    root.deiconify()


def hide():
    root.withdraw()


label1 = tk.Label(master=root, text='Loops', bg='red', fg='black')
label1.grid(row=0, column=0)
button1 = tk.Button(root, text="God Mode", bg='black', fg='white', command=multi_run_god)
button1.grid(row=1, column=0)
label3 = tk.Label(master=root, text='Misk', bg='red', fg='black')
label3.grid(row=6, column=0)
button11 = tk.Button(root, text="Calculator", bg='black', fg='white', command=open_calc)
button11.grid(row=7, column=0)
button12 = tk.Button(root, text="MSN", bg='black', fg='white', command=open_msn)
button12.grid(row=8, column=0)
button13 = tk.Button(root, text="Paint", bg='black', fg='white', command=open_paint)
button13.grid(row=9, column=0)

button20 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button20.grid(row=12, column=0)

label4 = tk.Label(master=root, text='Keybinds', bg='red', fg='black')
label4.grid(row=0, column=3)
label4 = tk.Label(master=root, text='C Show GUI', bg='red', fg='black')
label4.grid(row=1, column=3)
label5 = tk.Label(master=root, text='V Hide GUI', bg='red', fg='black')
label5.grid(row=2, column=3)
label6 = tk.Label(master=root, text='F1 KILLS LOOPS', bg='red', fg='black')
label6.grid(row=3, column=3)
label8 = tk.Label(master=root, text='F5 God Mode', bg='red', fg='black')
label8.grid(row=4, column=3)
label8 = tk.Label(master=root, text='K KYS', bg='red', fg='black')
label8.grid(row=5, column=3)

keyboard.add_hotkey("c", show)
keyboard.add_hotkey("v", hide)
keyboard.add_hotkey("k", kill_hack)
keyboard.add_hotkey("F2", god_mode)
root.mainloop()
