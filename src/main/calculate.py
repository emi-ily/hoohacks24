from flask import Flask


# the values are greenhouse gas emissions per serving of food, as calcualted in ReadCSVcarbondata.py
d = {'Cheese': 2.388, 'Coffee': 0.05706000000000001, 'Eggs': 0.467, 'Milk': 0.7875, 'Beef': 15.9168, 'Fish': 2.0445,
     'Lamb': 6.3552, 'Pork': 1.8465, 'Chicken': 1.5792}


def calculate_emissions(food, servings):
    return d[food] * servings

beefservings
