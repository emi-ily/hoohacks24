import pandas as pd

# this basically reads in two csv and ends up with a dictionary of food: GHG emissions per serving
# and then i use that dictionary in Calculations.Food.py


# source: https://www.datacamp.com/tutorial/pandas-read-csv
# also the data is GHG emissions per kg
usecols = ["Entity", "GHG emissions per kilogram (Poore & Nemecek, 2018)"]
df = pd.read_csv("carbondata.csv", usecols=usecols)
food = df.set_index('Entity').to_dict()['GHG emissions per kilogram (Poore & Nemecek, 2018)']
del food['Source: https://ourworldindata.org/environmental-impacts-of-food']
del food['Beef (dairy herd)']  # i just feel like this isn't useful

# keeping only the food we want to test
desired_keys = ['Beef (beef herd)', 'Cheese', 'Coffee', 'Eggs', 'Fish (farmed)', 'Lamb & Mutton', 'Milk', 'Pig Meat', 'Poultry Meat']
foods = {key: food[key] for key in desired_keys if key in food}
foods['Beef'] = foods.pop('Beef (beef herd)')
foods['Fish'] = foods.pop('Fish (farmed)')
foods['Lamb'] = foods.pop('Lamb & Mutton')
foods['Pork'] = foods.pop('Pig Meat')
foods['Chicken'] = foods.pop('Poultry Meat')
# print(foods)

# grams per serving (cooked)
# sources: https://www.eatforhealth.gov.au/food-essentials/how-much-do-we-need-each-day/serve-sizes#:~:text=A%20standard%20serve%20is%20(500,one%20small%20can%20of%20fish
# serving_size = {'Meat': 160, ''}
# classification = {'Meat': ['Beef', 'Pork', 'Chicken', 'Fish'], 'Dairy': ['Cheese', 'Milk']}

df = pd.read_csv("servingtograms.csv")
# print(df)
# food = df.set_index('Food').to_dict()['Grams', 'GHG']
food_dict = (df.set_index('Food')['KG'] * df.set_index('Food')['GHG']).to_dict()


# Convert the DataFrame to a dictionary
# food_dict = df.set_index('Food').T.to_dict('list')
print(food_dict)
