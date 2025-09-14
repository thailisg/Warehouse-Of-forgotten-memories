"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the interface or design for the use of the function that displays the Greek and Latin alphabets
"""

from logic import read_alphabet_csv, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX

import tkinter as tk
from tkinter import Frame, Label, Button
from tkinter import messagebox
import csv

class interface_alphabet:

    def __init__(self, greek_data, latin_data):
        """This function initialize the alphabet interface window."""

        #This create a new top level window for the greek and Latin alphabet
        self.interface = tk.Toplevel()
        self.interface.title("Greek and Latin Alphabets")
        self.interface.geometry("800x900")
        self.interface.config(bg = "#F4E1C1")

        #Title at the top of the window
        Label(self.interface, text = "Data that may be useful to you",bg = "#F4E1C1" ,font = ("book antiqua", 14)).pack(pady = 20, anchor = "center")

        #frame for the greek alphabet table
        greek_frame = Frame(self.interface, bg = "#e3d4b9", bd = 2, relief = "solid")
        greek_frame.place(relx = 0.3, rely = 0.5, anchor = "center")

        #Header for the greek table
        Label(greek_frame, text="Greek Alphabet", bg = "#e3d4b9", font = ("book antiqua", 14, "bold")).grid(row = 0, column = 0, columnspan = 2, pady = 10)

        #Columns for the greek table
        Label(greek_frame, text="Ancient", bg="#c2b280", font=("book antiqua", 12, "bold"), width=12).grid(row=1, column=0, padx=5, pady=3)
        Label(greek_frame, text="Actual", bg="#c2b280", font=("book antiqua", 12, "bold"), width=12).grid(row=1, column=1, padx=5, pady=3)

        #Populate Greek alphabet rows
        for i, (ancient, actual) in enumerate(greek_data, start=2):

            Label(greek_frame, text=ancient, bg="#e3d4b9", font=("book antiqua", 12), width=12).grid(row=i, column=0, padx=5, pady=1)
            Label(greek_frame, text=actual, bg="#e3d4b9", font=("book antiqua", 12), width=12).grid(row=i, column=1, padx=5, pady=1)

        #frame for the latin alphabet table
        latin_frame = Frame(self.interface, bg="#e3d4b9", bd=2, relief="solid")
        latin_frame.place(relx=0.7, rely=0.5, anchor="center")

        #Header for the latin table
        Label(latin_frame, text="Latin Alphabet", bg="#e3d4b9", font=("book antiqua", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        #Columns for the latin table
        Label(latin_frame, text="Actual", bg="#c2b280", font=("book antiqua", 12, "bold"), width=12).grid(row=1, column=0, padx=5, pady=3)
        Label(latin_frame, text="Ancient", bg="#c2b280", font=("book antiqua", 12, "bold"), width=12).grid(row=1, column=1, padx=5, pady=3)

        #Populate latin alphabet rows
        for i, (actual, ancient) in enumerate(latin_data, start=2):

            Label(latin_frame, text=actual, bg="#e3d4b9", font=("book antiqua", 12), width=12).grid(row=i, column=0, padx=5, pady=1)
            Label(latin_frame, text=ancient, bg="#e3d4b9", font=("book antiqua", 12), width=12).grid(row=i, column=1, padx=5, pady=1)

        self.interface.mainloop()



