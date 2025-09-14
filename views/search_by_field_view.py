"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the interface for the function that searches by field in the warehouse_objects.csv file
"""

from logic import search_by_field, \
    CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX, DESCRIPTION_INDEX

import tkinter as tk
from tkinter import Frame, Label, Button, Entry, Text, Scrollbar, Canvas
from tkinter import messagebox
import csv

class interface_search_by_field:

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
        """This Initialize the interface to search for objects by different fields and display results with description."""

        #This create a new top level window
        self.interface = tk.Toplevel()
        self.interface.title("Search by field")
        self.interface.geometry("800x520")
        self.interface.config(bg = "#F4E1C1")

        #Title at the top of the window
        Label(self.interface, text = "Type what you want to search for", bg = "#F4E1C1",font = ("book antiqua", 14)).pack(pady = 10, anchor = "center")

        #Search frame and button
        search_frame = Frame(self.interface, bg = "#F4E1C1")
        search_frame.pack(pady = 2)

        #Entry field for search text
        self.search_entry = Entry(search_frame, font = ("book antiqua", 12), width = 40)
        self.search_entry.pack(side = "left", padx = (0, 10))

        #Button to activate the search
        btn_search = Button(search_frame, text = "Search", font = ("book antiqua", 12), command = self.do_search)
        btn_search.pack(side = "left")

        #Canvas to display results with scrolling
        self.results_canvas = Canvas(self.interface, bg = "#d1ba9c", highlightthickness = 0)
        self.results_canvas.place(relx = 0.5, rely = 0.60, anchor = "center", width = 700, height = 350)

        #Scrollbar
        scrollbar = Scrollbar(self.interface, orient = "vertical", command = self.results_canvas.yview)
        scrollbar.place(relx = 0.98, rely = 0.60, anchor = "e", height = 350)

        self.results_canvas.configure(yscrollcommand=scrollbar.set)

        #Frame where the results will be added
        self.container_results = Frame(self.results_canvas, bg = "#d1ba9c")

        #Updates the scrollable area when the content changes
        self.container_results.bind(
        "<Configure>",
        lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )

        self.window_id = self.results_canvas.create_window((0, 0), window = self.container_results, anchor = "nw")

        #Makes the width of the inner content fit the width of the canvas
        self.results_canvas.bind(
        "<Configure>",
        lambda e: self.results_canvas.itemconfig(self.window_id, width = e.width)
        )

    def do_search(self):
        """Runs a search on the CSV file based on the text entered in the search field."""

        #Get the text the user typed and remove extra spaces
        search_value = self.search_entry.get().strip()

        #If the user did not enter anything, display a warning and exit.
        if not search_value:
            messagebox.showwarning("Warning", "Please enter a search value.")
            return

        #Fields to search
        field_to_search = [CODE_INDEX, NAME_INDEX, MATERIAL_INDEX, DATED_INDEX]

        #Calling the function to search the CSV
        results = search_by_field("archivos_CSV/warehouse_objects.csv", field_to_search, search_value)

        #Clear previous results
        for widget in self.container_results.winfo_children():

            widget.destroy()

        if not results:

            no_results_label = Label(self.container_results, bg = "#d1ba9c" ,text = "No results found.")
            no_results_label.pack()

            return

    #Show each result with its button to open the description
        for row in results:

            item_frame = Frame(self.container_results, bg = "#b49c7c", pady = 5)
            item_frame.pack(fill = "x", padx = 5, pady = 2)

            label_text = f"Code: {row[CODE_INDEX]} | Name: {row[NAME_INDEX]} | Date: {row[DATED_INDEX]}"
            label = Label(item_frame, text = label_text, bg = "#b49c7c", font = ("book antiqua", 12), anchor = "w")
            label.pack(side = "left", fill = "x", expand = True, padx = 5)

            btn_desc = Button(item_frame, text="Description", font=("book antiqua", 10), bg="#333333", fg="white",
                command=lambda desc=row[DESCRIPTION_INDEX], mat=row[MATERIAL_INDEX]: self.show_description(desc, mat))
            btn_desc.pack(side = "right", padx = 5)