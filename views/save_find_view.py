"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the interface for the function that adds new objects to the warehouse_objects.csv file
"""

from logic import save_find, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX

import tkinter as tk
from tkinter import Frame, Label, Button, Entry, Text
from tkinter import messagebox
import csv

class interface_save_find:

    def __init__(self):
        """Initialize the window to save a new object"""

        #This create a new top level window
        self.interface = tk.Toplevel()
        self.interface.title("Add new object")
        self.interface.geometry("800x520")
        self.interface.configure(bg = "#F4E1C1")

        #Title at the top of the window
        Label(self.interface, text = "Fill out the form", bg = "#F4E1C1", font = ("book antiqua", 14)).pack(pady = 20, anchor = "center")

        #frame for the form
        container_form = Frame(self.interface, bg = "#d1ba9c", highlightbackground = "#6b6b6b", highlightthickness = 2)
        container_form.place(relx = 0.5, rely = 0.55, anchor = "center", width = 600, height = 350)

        def add_placeholder_entry(entry: tk.Entry, placeholder: str): 
            """Adds gray text inside the Entry that disappears when typing.Displays the placeholder when the field is empty, 
            and hides it when the user starts typing"""

            entry.insert(0, placeholder)
            entry.config(fg = "gray")

            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, tk.END)
                    entry.config(fg = "black")

            def on_focus_out(event):
                if not entry.get():
                    entry.insert(0, placeholder)
                    entry.config(fg = "gray")

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)

        def add_placeholder_text(text_widget: tk.Text, placeholder: str): 
            """Displays gray text inside the Text widget that disappears when typing.If the widget is empty, it displays the placeholder, and when the user types,
            it clears it so only the actual text remains."""

            text_widget.insert("1.0", placeholder)
            text_widget.config(fg = "gray")

            def on_focus_in(event):

                if text_widget.get("1.0", "end-1c") == placeholder:
                    text_widget.delete("1.0", tk.END)
                    text_widget.config(fg = "black")

            def on_focus_out(event):

                if not text_widget.get("1.0", "end-1c").strip():
                    text_widget.insert("1.0", placeholder)
                    text_widget.config(fg = "gray")

            text_widget.bind("<FocusIn>", on_focus_in)
            text_widget.bind("<FocusOut>", on_focus_out)

        #Code entry
        code_entry = Entry(container_form, font = ("book antiqua", 12), width = 40)
        code_entry.pack(pady = (10,5))
        add_placeholder_entry(code_entry, "Write the code")

        #Name entry
        name_entry = Entry(container_form, font = ("book antiqua", 12), width = 40)
        name_entry.pack(pady = 5)
        add_placeholder_entry(name_entry, "Write the name of the object")

        #Material entry
        material_entry = Entry(container_form, font = ("book antiqua", 12), width = 40)
        material_entry.pack(pady = 5)
        add_placeholder_entry(material_entry, "Write the material")

        #Date entry
        date_entry = Entry(container_form, font = ("book antiqua", 12), width = 40)
        date_entry.pack(pady = 5)
        add_placeholder_entry(date_entry, "Write the dated")

        #Frame for description and scrollbar are together
        desc_frame = Frame(container_form)
        desc_frame.pack(pady = 10)

        #Text widget for description
        description_entry = Text(desc_frame, font = ("book antiqua", 12), width = 45, height = 6, wrap = "word")
        description_entry.pack(side = "left")
        add_placeholder_text(description_entry, "Write the description of the object")

        #Scrollbar for description
        scrollbar = tk.Scrollbar(desc_frame, command = description_entry.yview)
        scrollbar.pack(side = "left", fill = "y")
        description_entry.config(yscrollcommand = scrollbar.set)

        def save_data():
            """Verify that the form data is complete and save the record in the CSV."""

            #Get what the user typed in each form field
            code = code_entry.get()
            name = name_entry.get()
            material = material_entry.get()
            dated = date_entry.get()
            description = description_entry.get("1.0", "end-1c")

            #List of example texts and what the person typed to check if any field is empty
            placeholders = [
                ("Write the code", code),
                ("Write the name of the object", name),
                ("Write the material", material),
                ("Write the dated (YYYY-MM-DD)", dated),
                ("Write the description of the object", description)
                ]
            
            #Validate empty fields or fields with placeholders
            for ph, val in placeholders:

                if val == ph or val.strip() == "":

                    messagebox.showwarning("Warning", f"Please fill out the field: {ph}")

                    return

            #Save the record using the save_find function of the logic module
            error = save_find("archivos_CSV/warehouse_objects.csv", code, name, material, dated, description)

            if error:

                #error message in case writing fails
                messagebox.showerror("Error saving file", error)

            else:
                
                #Confirm success and close window
                messagebox.showinfo("Success", "Object saved successfully!")
                self.interface.destroy()

        # Save button
        btn_save = Button(container_form, text = "Save", font = ("book antiqua", 14), width = 20, command = save_data)
        btn_save.pack(pady = 15)
