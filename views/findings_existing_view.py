"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the interface for the function that reads the file where the objects are stored (warehouse_objects.csv)
"""

import tkinter as tk
from tkinter import Frame, Label, Button, Text, Canvas, Scrollbar
from logic import read_findings_existing, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX
from tkinter import messagebox
import csv

class interface_findings_existing:

    def show_description(self, description, material):
        """This function is to opens a new window showing the detailed description of a finding"""

        #This create a new top level window apart from the main one for show the description, since they are archaeological objects, they may require long descriptions
        descripcion_interface = tk.Toplevel()
        descripcion_interface.title("Description")
        descripcion_interface.geometry("400x300")
        descripcion_interface.configure(bg="#f0f0f0")

        #This is a text widget to display the description with scrollbar
        text_area = Text(descripcion_interface, wrap = "word", font=("book antiqua", 12), bg = "#ffffff")
        text_area.pack(expand = True, fill = "both", padx = 10, pady = 10)

        #scrollbar
        scroll = Scrollbar(text_area)
        scroll.pack(side = "right", fill = "y")
        text_area.config(yscrollcommand = scroll.set)
        scroll.config(command = text_area.yview)

        full_text = f"Material: {material}\n\n{description}"

        #This insert description and disable editing
        text_area.insert("1.0", full_text)
        text_area.config(state="disabled")

    def __init__(self):
        """This initializes the interface window listing all findings"""

        #This create a new top level window
        self.interface = tk.Toplevel()
        self.interface.title("View findings")
        self.interface.geometry("800x520")
        self.interface.configure(bg = "#F4E1C1")

        #Title at the top of the window
        Label(self.interface, text = "Store",bg = "#F4E1C1", font = ("book antiqua", 14)).pack(pady = 40, anchor = "center")

        #Canvas widget to allow scrolling objects
        container_canvas = Canvas(self.interface, bg = "#d1ba9c", highlightthickness = 0)
        container_canvas.place(relx = 0.5, rely = 0.50, anchor = "center", width = 600, height = 325)

        #Scrollbar
        scrollbar = Scrollbar(self.interface, orient = "vertical", command = container_canvas.yview)
        scrollbar.place(relx = 0.98, rely = 0.55, anchor = "e", height = 350)

        container_canvas.configure(yscrollcommand = scrollbar.set)

        #Frame that would contain the objects
        container_objects = Frame(container_canvas, bg="#d1ba9c", highlightbackground="#6b6b6b", highlightthickness=2)
        inner_frame_id = container_canvas.create_window((0, 0), window=container_objects, anchor="nw")

        def on_frame_configure(event):
            """This adjusts the scroll area to include everything within the frame"""

            container_canvas.configure(scrollregion=container_canvas.bbox("all"))

        def resize_inner_frame(event):
            """Makes the inner frame always have the same width as the canvas."""

            container_canvas.itemconfig(inner_frame_id, width=event.width)

        # Bind events
        container_objects.bind("<Configure>", on_frame_configure)
        container_canvas.bind("<Configure>", resize_inner_frame)

        #Read findings data from CSV file
        read_csv, error_msg = read_findings_existing("archivos_CSV/warehouse_objects.csv", CODE_INDEX)

        if error_msg:

            messagebox.showerror("Error loading file", error_msg)

        y_offset = 10
        
        #Populate the frame with each finding
        for key, row in read_csv.items():

            item_frame = Frame(container_objects, bg = "#b49c7c")
            item_frame.pack(pady = 5, padx = 10, fill = "x")

            label_text = f"{row[CODE_INDEX]} | {row[NAME_INDEX]} | Date: {row[DATED_INDEX]}"

            Label(item_frame, text=label_text, fg = "white", bg = "#b49c7c",
            font = ("book antiqua", 12), anchor = "w").pack(side = "left", fill = "both", expand = True, padx = 10)

            btn_desc = Button(item_frame, text="Description", font=("book antiqua", 10), bg="#333333", fg="white",
                command=lambda desc=row[DESCRIPTION_INDEX], mat=row[MATERIAL_INDEX]: self.show_description(desc, mat))
            
            btn_desc.pack(side="right", padx = 10)

        