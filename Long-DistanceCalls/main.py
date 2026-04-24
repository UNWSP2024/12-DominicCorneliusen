#Title: Long-Distance Calls
#Author: Dominic Corneliusen
#Date last modified: 4/23/2026

#Start
import tkinter
from tkinter import messagebox

class myGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Long-Distance Call Calculator")

        self.rate_frame = tkinter.Frame(self.window)
        self.entry_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        self.rate_frame.pack(pady=10)
        self.entry_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        self.rate_var = tkinter.IntVar()
        self.rate_var.set(1)

        tkinter.Radiobutton(self.rate_frame, text="Daytime (0.02/min)",
                            variable=self.rate_var, value=1).pack(anchor="w")
        tkinter.Radiobutton(self.rate_frame, text="Evening (0.12/min)",
                            variable=self.rate_var, value=2).pack(anchor="w")
        tkinter.Radiobutton(self.rate_frame, text="Off-Peak (0.05/min)",
                            variable=self.rate_var, value=3).pack(anchor="w")

        self.label_minutes = tkinter.Label(self.entry_frame, text="Minutes:")
        self.entry_minutes = tkinter.Entry(self.entry_frame, width=10)

        self.label_minutes.pack()
        self.entry_minutes.pack()

        self.calc_button = tkinter.Button(self.button_frame, text="Calculate Charge", command=self.calculate_charge)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.window.destroy)

        self.calc_button.pack(side="left", padx=5)
        self.quit_button.pack(side="right", padx=5)

        tkinter.mainloop()
    def calculate_charge(self):
        try:
            minutes = float(self.entry_minutes.get())
            if self.rate_var.get() == 1:
                rate = 0.02
            elif self.rate_var.get() == 2:
                rate = 0.12
            else:
                rate = 0.05
            total = minutes * rate
            messagebox.showinfo("Call Charge", f"Total Charge: ${total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of minutes.")
if __name__ == "__main__":
    my_gui = myGUI()