"""
data_manager.py
AnimalShelter
Zeina Douglas & Sameeha Fatima

Saves and loads the list of animals and all the data using pickle.
"""

import os
import pickle

# the file where the animals are saved
FILE_NAME = "animaldata.pkl"

class DataManager:

    def __init__(self, file_name = FILE_NAME):
        self.file_name = file_name
        self.animals = []
        self.load()


    # loads in all the saved animals in the pickle file
    def load(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, "rb") as f:
                self.animals = pickle.load(f)
        else:
            self.animals = []


    # saves all the animals to the pickle file
    def save(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self.animals, f)


    # gives a new id that no other animal is using
    def give_animal_id(self):
        pass


    # adds a new animal, gives it an id, and saves it into the pickle file
    def add_animal(self, animal):
        pass


    # gets back a copy of the list of all animals stored
    def get_all(self):
        pass

  
    # finds an animal by its id
    def find_animal(self, animal_id):
        pass


    # replaces the saved animal that has the same id
    def update_animal(self, updated_animal):
        pass


    # removes the animal with this id
    def delete_animal(self, animal_id):
        pass

