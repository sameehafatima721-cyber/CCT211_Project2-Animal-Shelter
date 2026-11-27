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
        pass

    # updating the table
    def refresh_table(self):
        pass

    # searching for the animasl that match the users input and displays them in the table
    def search_animals(self):
        pass

    # checking the row the user selected and deletes an animal
    def delete_animal(self):
        pass

   # opens up the animal form
    def add_animal(self):
        pass
 
    # edits the animal by opening the animal form with its saved data
    def edit_animal(self):
        pass
   
    # opens up the stats window and displays the charts
    def open_stats(self):
        pass
