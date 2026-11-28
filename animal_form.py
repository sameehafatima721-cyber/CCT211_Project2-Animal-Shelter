"""
animal_form.py
AnimalShelter
Zeina Douglas & Sameeha Fatima

The window where the user adds a new animal or edits an old one.
"""

import tkinter as tk
import tkinter.scrolledtext as st
from animal import *


class AnimalForm:

    def __init__(self, parent, data_manager, refresh_list, animal = None):
        self.data_manager = data_manager
        self.refresh_list = refresh_list
        self.animal = animal

        # making the form have a top level window
        self.window = tk.Toplevel(parent)

        # creating an appropraite title based on animal amount
        if animal is None:
            self.window.title("Add Animal")
        else:
            self.window.title("Edit Animal")
        self.window.resizable(0, 0)

        # every data in the form gets a text container which will all be kept in one dictionary
        self.data = {}
        self.data["Name"] = tk.StringVar()
        self.data["Species"] = tk.StringVar()
        self.data["Age"] = tk.StringVar()
        self.data["Weight"] = tk.StringVar()
        self.data["Weight unit"] = tk.StringVar()
        self.data["Intake date"] = tk.StringVar()
        self.data["Status"] = tk.StringVar()
        self.data["Vaccination"] = tk.StringVar()
       
        # the dropdowns start on their first choice
        self.data["Species"].set(SPECIES[0])
        self.data["Weight unit"].set(WEIGHT_UNITS[0])
        self.data["Status"].set(STATUSES[0])
        self.data["Vaccination"].set(VACCINATION[0])

        # make widgets
        self.make_widgets()


    # making all the widgets needed for the form
    def make_widgets(self):
        window = self.window

        # name
        name_label = tk.Label(window, text="Name")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        name_entry = tk.Entry(window, width=30, textvariable=self.data["Name"])
        name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        # species
        species_label = tk.Label(window, text="Species")
        species_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        species_menu = tk.OptionMenu(window, self.data["Species"], *SPECIES)
        species_menu.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        # age
        age_label = tk.Label(window, text="Age (yrs)")
        age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        age_entry = tk.Entry(window, width=30, textvariable=self.data["Age"])
        age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        # weight
        weight_label = tk.Label(window, text="Weight")
        weight_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        weight_entry = tk.Entry(window, width=30, textvariable=self.data["Weight"])
        weight_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")
        unit_menu = tk.OptionMenu(window, self.data["Weight unit"], *WEIGHT_UNITS)
        unit_menu.grid(row=3, column=2, padx=10, pady=5, sticky="we")

        # intake date
        date_label = tk.Label(window, text="Intake date (YYYY-MM-DD)")
        date_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        date_entry = tk.Entry(window, width=30, textvariable=self.data["Intake date"])
        date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="we")

        # status
        status_label = tk.Label(window, text="Status")
        status_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        status_menu = tk.OptionMenu(window, self.data["Status"], *STATUSES)
        status_menu.grid(row=5, column=1, padx=10, pady=5, sticky="we")

        # vaccination
        vacc_label = tk.Label(window, text="Vaccination")
        vacc_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        vacc_menu = tk.OptionMenu(window, self.data["Vaccination"], *VACCINATION)
        vacc_menu.grid(row=6, column=1, padx=10, pady=5, sticky="we")

        # notes
        notes_label = tk.Label(window, text="Notes")
        notes_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.notes_text = st.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        self.notes_text.grid(row=8, column=0, columnspan=3, padx=10, pady=5, sticky="we")

        # save and cancel buttons
        save_button = tk.Button(window, text="Save", command=self.save_animal)
        save_button.grid(row=9, column=0, padx=10, pady=10)
        cancel_button = tk.Button(window, text="Cancel", command=window.destroy)
        cancel_button.grid(row=9, column=1, padx=10, pady=10)


    # puts the animal being edited into the boxes filled and its used for when the user edits
    def fill_form(self):
        pass


    # saves the animal
    def save_animal(self):
       pass


    # checks if the users input is valid 
    def check_form(self):
        pass

