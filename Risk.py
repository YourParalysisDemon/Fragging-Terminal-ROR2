import keyboard
import tkinter as tk
import webbrowser
import pymem.exception
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from subprocess import Popen


mem = Pymem("Risk of Rain 2.exe")
module = module_from_name(mem.process_handle, "UnityPlayer.dll").lpBaseOfDll
money_offsets = [0x8, 0x10, 0x50, 0x70, 0x28, 0x48, 0xB4]
health_offsets = [0X0, 0X10, 0X30, 0X108, 0X28, 0X68]
kill_offsets = [0x10, 0xC0, 0X28, 0X20, 0X58, 0XB0, 0X68]
fire_offsets = [0x0, 0x10, 0X30, 0XA8, 0X28, 0X80]
shield_offsets = [0X0, 0x10, 0X30, 0X48, 0X28, 0XB0, 0X6C]
ice_offsets = [0x0, 0x10, 0x30, 0xC8, 0xD8, 0x28, 0x80]
x_offsets = [0X8, 0X10, 0X30, 0X28, 0X28, 0X30, 0X254]
y_offsets = [0x0, 0x10, 0x30, 0x1B8, 0X90, 0X28, 0X25C]
z_offsets = [0x0, 0x10, 0x30, 0x1A8, 0xE8, 0x258]


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


def multi_run_god():
    new_thread = Thread(target=go_fly(), daemon=True)
    new_thread.start()


def go_fly():
    addr1 = getpointeraddress(module + 0X017DCA98, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42820000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def tele_up():
    addr = getpointeraddress(module + 0X017DCA98, z_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x42820000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def money_hack():
    addr = getpointeraddress(module + 0x018178E0, money_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0X2097252)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def shield_hack():
    addr = getpointeraddress(module + 0x017DCA98, shield_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x43960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def ice_hack():
    addr = getpointeraddress(module + 0x017DCA98, ice_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0X2097252)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def kill_hack():
    addr = getpointeraddress(module + 0x017DCA98, health_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x0)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def give_fire():
    addr = getpointeraddress(module + 0x017DCA98, fire_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x43960000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")


def health_hack():
    addr = getpointeraddress(module + 0x017DCA98, health_offsets)
    if addr is not None:
        try:
            mem.write_int(addr, 0x47960000)
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
button1 = tk.Button(root, text="Go Fly?", bg='black', fg='white', command=multi_run_god)
button1.grid(row=1, column=0)
label3 = tk.Label(master=root, text='Misk', bg='red', fg='black')
label3.grid(row=6, column=0)
button11 = tk.Button(root, text="Calculator", bg='black', fg='white', command=open_calc)
button11.grid(row=7, column=0)
button12 = tk.Button(root, text="MSN", bg='black', fg='white', command=open_msn)
button12.grid(row=8, column=0)
button13 = tk.Button(root, text="Paint", bg='black', fg='white', command=open_paint)
button13.grid(row=9, column=0)

label3 = tk.Label(master=root, text='Non Loops', bg='red', fg='black')
label3.grid(row=0, column=2)
button14 = tk.Button(root, text="Money", bg='black', fg='white', command=money_hack)
button14.grid(row=1, column=2)
button15 = tk.Button(root, text="Primary-Ammo", bg='black', fg='white', command=give_fire)
button15.grid(row=2, column=2)
button16 = tk.Button(root, text="Ice-Wall", bg='black', fg='white', command=ice_hack)
button16.grid(row=3, column=2)
button17 = tk.Button(root, text="Shield", bg='black', fg='white', command=shield_hack)
button17.grid(row=4, column=2)
button18 = tk.Button(root, text="KYS", bg='black', fg='white', command=kill_hack)
button18.grid(row=5, column=2)
button18 = tk.Button(root, text="Health", bg='black', fg='white', command=health_hack)
button18.grid(row=6, column=2)

label1 = tk.Label(master=root, text='Tele options', bg='red', fg='black')
label1.grid(row=3, column=0)
button23 = tk.Button(root, text="Tele up", bg='black', fg='white', command=tele_up)
button23.grid(row=4, column=0)

button20 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button20.grid(row=8, column=2)

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
label8 = tk.Label(master=root, text='Z Tele-Up', bg='red', fg='black')
label8.grid(row=6, column=3)
label9 = tk.Label(master=root, text='F2 Fly', bg='red', fg='black')
label9.grid(row=7, column=3)

keyboard.add_hotkey("c", show)
keyboard.add_hotkey("v", hide)
keyboard.add_hotkey("F5", health_hack)
keyboard.add_hotkey("k", kill_hack)
keyboard.add_hotkey("z", tele_up)
keyboard.add_hotkey("F2", go_fly)
root.mainloop()
