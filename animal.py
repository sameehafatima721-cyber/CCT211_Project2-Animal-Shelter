"""
animal.py
AnimalShelter
Zeina Douglas & Sameeha Fatima

Stores the animal records for the app.
"""

# all the choices we use which will be included in the dropdown menus
SPECIES = ["Dog", "Cat", "Bird", "Rabbit", "Hamster", "Guinea pig", "Turtle"]
STATUSES = ["Available", "Medical hold", "Adopted"]
VACCINATION = ["Up to date", "Partial", "Not vaccinated"]
WEIGHT_UNITS = ["g", "kg"]

# stores the information about one animal
class Animal:

    def __init__(self, animal_id, name, species, age, weight, weight_unit, intake_date, status, vaccination, notes=""):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
        self.weight_unit = weight_unit
        self.intake_date = intake_date
        self.status = status
        self.vaccination = vaccination
        self.notes = notes
        
