"""
shelter_app.py
AnimalShelter
Sameeha Fatima & Zeina Douglas


In charge of managing and displaying the screens
"""

import tkinter as tk
from tkinter import ttk, messagebox

# creating the class
class ShelterApp:
    def __init__(self, root, data_manager):
        self.root = root
        self.data_manager = data_manager

        self.root.title("Shelter Manager")
        self.root.geometry("900x600")

        # creating the main interface and displaying the animals
        self.make_widgets()
        self.refresh_table()

    # making the interface
    def make_widgets(self):
        title_label = tk.Label(self.root, text = "Animal Shelter Manager")
        title_label.pack(pady = 10)
        
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady = 10)
        
        tk.Label(search_frame, text = "Search:").pack(side = "left")
        
        self.search_entry = tk.Entry(search_frame, width = 30)
        self.search_entry.pack(side = "left", padx = 5)
        
        # searching
        search_button = tk.Button(search_frame, text = "Search", command = self.search_animals)
        search_button.pack(side = "left", padx = 5)
        
        # clearing 
        clear_button = tk.Button(search_frame, text = "Show All", command = self.refresh_table)
        clear_button.pack(side = "left", padx = 5)
        
        # creating the table
        columns = ("ID", "Name", "Species", "Age", "Weight", "Intake Date", "Status")
        
        # creating the treeview
        self.tree = ttk.Treeview(self.root, columns = columns, show = "headings")
        
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=120, anchor="center")
        
            self.tree.pack(fill="both", expand=True, padx=15, pady=10)
        
            # buttons
            button_frame = tk.Frame(self.root)
            button_frame.pack(pady = 10)
        
            # placing the buttons on the screen
            tk.Button(button_frame, text = "Add an Animal", command = self.add_animal).pack(side = "left", padx = 10)
            tk.Button(button_frame, text = "Edit Animal", command = self.edit_animal).pack(side = "left", padx = 10)
            tk.Button(button_frame, text = "Delete an Animal", command = self.delete_animal).pack(side = "left", padx = 10)
            tk.Button(button_frame, text = "Statistics", command = self.open_stats).pack(side = "left", padx = 10)
        
    # updating the table
    def refresh_table(self):
        # removing the old rows
                for item in self.tree.get_children():
                    self.tree.delete(item)
        
                # getting animals from the DataManager class
                animals = self.data_manager.get_all()
        
                # inserting animals into the table
                for animal in animals:
                    weight_display = str(animal.weight) + " " + animal.weight_unit
        
                    self.tree.insert("", "end", values = (
                        animal.animal_id,
                        animal.name,
                        animal.species,
                        animal.age,
                        weight_display,
                        animal.intake_date,
                        animal.status
                    ),
                    tags = (animal.status,)
                    )

    # searching for the animasl that match the users input and displays them in the table
    def search_animals(self):
        search_text = self.search_entry.get().lower()

        # clearing the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # getting all animals
        animals = self.data_manager.get_all()

        # searching for animals that match
        for animal in animals:

            if (
                search_text in str(animal.animal_id).lower()
                or search_text in animal.name.lower()
                or search_text in animal.species.lower()
                or search_text in animal.status.lower()
            ):
                weight_display = str(animal.weight) + " " + animal.weight_unit
                self.tree.insert(
                    "", "end", values = (
                        animal.animal_id,
                        animal.name,
                        animal.species,
                        animal.age,
                        weight_display,
                        animal.intake_date,
                        animal.status
                    ),
                    tags = (animal.status,)
                )

    # checking the row the user selected and deletes an animal
    def delete_animal(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an animal to delete")
            return
        row = self.tree.item(selected_item[0])
        animal_id = row["values"][0]

        # asking for a confirmation
        answer = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this animal?")

        if answer:
            self.data_manager.delete_animal(animal_id)
            self.refresh_table()

   # opens up the animal form
    def add_animal(self):
        pass
 
 	# edits the animal by opening the animal form with its saved data
    def edit_animal(self):
        pass
   
    # opens up the stats window and displays the charts
    def open_stats(self):
        pass
