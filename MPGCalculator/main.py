#Title: MPG Calculator
#Author: Dominic Corneliusen
#Date last modified: 4/23/2026

#Start
import tkinter
from tkinter import messagebox

class myGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("MPG Calculator")

        self.entry_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        self.entry_frame.pack(pady=10)
        self.button_frame.pack(pady=10)

        self.Label1 = tkinter.Label(self.entry_frame, text="Miles")
        self.entry_box = tkinter.Entry(self.entry_frame, width=10)

        self.Label2 = tkinter.Label(self.entry_frame, text="Gallons")
        self.entry_box2 = tkinter.Entry(self.entry_frame, width=10)

        self.Label1.pack()
        self.entry_box.pack()
        self.Label2.pack()
        self.entry_box2.pack()

        self.button = tkinter.Button(self.button_frame, text="Calculate", command=self.calculate_wrapper)
        self.quitButton = tkinter.Button(self.button_frame, text="Quit", command=self.window.destroy)

        self.button.pack(side="left", padx=5)
        self.quitButton.pack(side="right", padx=5)

        tkinter.mainloop()

    def calculateMPG(self, miles, gallons):
        MPG = miles / gallons
        messagebox.showinfo("Calculate MPG", "MPG = " + str(MPG))

    def calculate_wrapper(self):
        try:
            miles = float(self.entry_box.get())
            gallons = float(self.entry_box2.get())
            self.calculateMPG(miles, gallons)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Gallons cannot be zero.")

if __name__ == "__main__":
    my_gui = myGUI()
