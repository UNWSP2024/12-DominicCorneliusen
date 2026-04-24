#Title: Joe's Automotive
#Author: Dominic Corneliusen
#Date last modified: 4/23/2026

#Start
import tkinter
from tkinter import messagebox

class myGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Joe's Automotive")

        self.service_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        self.service_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.rad_var = tkinter.IntVar()
        self.trans_var = tkinter.IntVar()
        self.insp_var = tkinter.IntVar()
        self.muff_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()

        tkinter.Checkbutton(self.service_frame, text="Oil Change ($30)", variable=self.oil_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Lube Job ($20)", variable=self.lube_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Radiator Flush ($40)", variable=self.rad_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Transmission Fluid ($100)", variable=self.trans_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Inspection ($35)", variable=self.insp_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Muffler Replacement ($200)", variable=self.muff_var).pack(anchor="w")
        tkinter.Checkbutton(self.service_frame, text="Tire Rotation ($20)", variable=self.tire_var).pack(anchor="w")

        self.calc_button = tkinter.Button(self.button_frame, text="Calculate Total", command=self.calculate_total)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.window.destroy)
        self.calc_button.pack(side="left", padx=5)
        self.quit_button.pack(side="right", padx=5)

        tkinter.mainloop()
    def calculate_total(self):
        total = 0
        if self.oil_var.get() == 1:
            total += 30
        if self.lube_var.get() == 1:
            total += 20
        if self.rad_var.get() == 1:
            total += 40
        if self.trans_var.get() == 1:
            total += 100
        if self.insp_var.get() == 1:
            total += 35
        if self.muff_var.get() == 1:
            total += 200
        if self.tire_var.get() == 1:
            total += 20
        messagebox.showinfo("Total Charges", f"Total: ${total}")

if __name__ == "__main__":
    my_gui = myGUI()
