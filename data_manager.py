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
        current_id = 0
        for animal in self.animals:
            if animal.animal_id > current_id:
                current_id = animal.animal_id
        return current_id + 1


    # adds a new animal, gives it an id, and saves it into the pickle file
    def add_animal(self, animal):
        animal.animal_id = self.give_animal_id()
        self.animals.append(animal)
        self.save()
        return animal


    # gets back a copy of the list of all animals stored
    def get_all(self):
        return list(self.animals)


    # finds an animal by its id
    def find_animal(self, animal_id):
        for animal in self.animals:
            if animal.animal_id == animal_id:
                return animal
        return None #returns none if there isnt an animal found


    # replaces the saved animal that has the same id
    def update_animal(self, updated_animal):
        for i in range(len(self.animals)):
            if self.animals[i].animal_id == updated_animal.animal_id:
                self.animals[i] = updated_animal
                self.save()
                return True
        return False


    # removes the animal with this id
    def delete_animal(self, animal_id):
        animal = self.find_animal(animal_id)
        if animal is None:
            return False
        self.animals.remove(animal)
        self.save()
        return True 
