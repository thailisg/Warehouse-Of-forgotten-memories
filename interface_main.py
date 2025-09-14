"""
Author: Thailis Gonzalez
Purpose: Contain the main design of the application where the buttons to access the functions are located.
"""

from views.findings_existing_view import interface_findings_existing
from views.save_find_view import interface_save_find
from views.search_by_field_view import interface_search_by_field
from views.alphabet_csv_view import interface_alphabet
from views.delete_view import interface_delete_find

from logic import read_alphabet_csv

import tkinter as tk
from tkinter import Frame, Label, Button
import csv

class design_main:

    def __init__(self):

        """Function that initialize the main application window"""
        
        #Main window
        self.root = tk.Tk()
        self.root.geometry("800x520")
        self.root.title("Warehouse of Forgotten Memories")

        #Container main
        self.frm_main = Frame(self.root)
        self.frm_main.pack(fill=tk.BOTH,expand=True)

        #Left frame to contain the image
        self.frm_left = Frame(self.frm_main, width=180, bg="#d2b48c")
        self.frm_left.pack(side=tk.LEFT, fill=tk.Y)

        #Right frame to contain the buttons
        self.frm_right = Frame(self.frm_main, bg="#F4E1C1")
        self.frm_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #Load the image to decorate the main window in Left frame
        self.image = tk.PhotoImage(file="Assets/archaeological.png")
        self.lbl_image = Label(self.frm_left, image=self.image, bg="#d2b48c")
        self.lbl_image.image = self.image
        self.lbl_image.pack(padx=10, pady=10)

        #Brings content to the right frame
        self.setup_main(self.frm_right)

        self.root.mainloop()

    def setup_main(self, frm):
        """Adds a welcome label and four buttons, each linked to different interfaces"""
        
        #Title of the program in the interface
        lbl_sides = Label(frm, text="Welcome to Warehouse of Forgotten Memories", bg="#F4E1C1", font=("book antiqua", 18, "bold"), anchor="center", wraplength=400,
            justify="center")
        lbl_sides.pack(fill=tk.X, pady=20)

        #Buttons
        frm_buttons = Frame(frm, bg="#F4E1C1")
        frm_buttons.pack(pady=30)

        #Button 1: this is to see all existing objects
        btn_finding_existing = Button(frm_buttons, text="View findings", font=("book antiqua", 14), width=20,command=lambda: interface_findings_existing())
        btn_finding_existing.pack(pady=5)

        #Button 2: this is to add a new object 
        btn_save_find = Button(frm_buttons, text="Add new object", font=("book antiqua", 14), width=20, command=lambda: interface_save_find())
        btn_save_find.pack(pady=5)

        #Button 3: this is to search by field
        btn_search_by_field = Button(frm_buttons, text="Search by field", font=("book antiqua", 14), width=20, command=lambda: interface_search_by_field())
        btn_search_by_field.pack(pady=5)

        #Button 4: this takes you to a page with two tables where you can see two alphabets
        btn_read_alphabet = Button(frm_buttons, text="Useful data", font=("book antiqua", 14), width=20, command=self.open_interface_alphabet)
        btn_read_alphabet.pack(pady=5)

        #Button 5: this is to delete an object from warehouse_objects.csv
        btn_delete = Button(frm_buttons, text="Delete object", font=("book antiqua", 14), width=20, command = lambda: interface_delete_find())
        btn_delete.pack(pady=5)

    def open_interface_alphabet(self):
        """This function reads the CSV files greek.csv and latin.csv and fetches the interface_alphabet class for the interfacee"""

        greek_data = read_alphabet_csv("archivos_CSV/greek.csv")
        latin_data = read_alphabet_csv("archivos_CSV/latin.csv")

        interface_alphabet(greek_data, latin_data)