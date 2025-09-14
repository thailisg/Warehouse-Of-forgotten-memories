"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the interface for the delete object function
"""

import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox
from logic import delete_find, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX

class interface_delete_find:

    def __init__(self):
        """initializes the window to delete some stored object through code"""

        #This create a new top level window
        self.interface = Toplevel()
        self.interface.title("Delete Finding")
        self.interface.geometry("350x150")
        self.interface.config(bg = "#F4E1C1")

        #label that tells the user what to do
        Label(self.interface, text = "Enter the code of the element to delete:", bg = "#F4E1C1", font = ("book antiqua", 12)).pack(pady = 15)

        #Entry to write the code of the object to eliminate
        self.code_entry = Entry(self.interface, font=("book antiqua", 14), width = 25)
        self.code_entry.pack(pady = 5)

        #Red Button to delete
        btn_delete = Button(self.interface, text="Delete", font = ("book antiqua", 12), bg = "red", fg = "white", command = self.delete_record)
        btn_delete.pack(pady = 10)

    def delete_record(self):
        """This function take the code the user wrote and delete the corresponding object"""

        #This get the code and delete extra spaces
        code_to_delete = self.code_entry.get().strip()

        #Only in case the code is not entered
        if not code_to_delete:
            messagebox.showwarning("Warning", "Please enter a code.")
            return

        #Confirmation for the user to know if they really want to delete the object
        answer = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete record with code '{code_to_delete}'?")
        if not answer:
            return

        error_message = delete_find("archivos_CSV/warehouse_objects.csv", code_to_delete)

        if error_message:

            messagebox.showerror("Error", error_message)

        else:
            
            messagebox.showinfo("Success", f"Record with code '{code_to_delete}' deleted successfully.")
            self.interface.destroy()