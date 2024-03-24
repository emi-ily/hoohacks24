from flask import Flask, render_template, request
import openfoodfacts
import json
import re

def search_product(product_name):
    api = openfoodfacts.API(user_agent="OPenFoodInfo/1.0")
    data = api.product.text_search(product_name)
    return int(data["count"])

def get_product_info(product_name):
    api = openfoodfacts.API(user_agent="OPenFoodInfo/1.0")
    data = api.product.text_search(product_name)

    with open('info.json', 'w') as f:
        json.dump(data, f, indent=4)

    product = data['products'][0]

    ecoscore = str(product.get('ecoscore_data').get('grades').get('world'))
    ecoscore = ecoscore.upper()
    print("Eco-score:", ecoscore)

    nutriscore = str(product.get('nutrition_grades_tags'))
    nutriscore = " ".join(re.findall("[a-zA-Z]+", nutriscore)).upper()
    print("Nutri-score:", nutriscore)

    nutriments = str(product.get('nutriments'))

    #print("Proteins:", product.get('nutriments').get('proteins'), "g")
    #print("Carbohydrates:", product.get('nutriments').get('carbohydrates'), "g")
    #print("Sugar:", product.get('nutriments').get('sugars'), "g")
    #print("Fat:", product.get('nutriments').get('fat'), "g")
    #print("Carbon Footprint From Known Ingredients:", product.get('nutriments').get('carbon-footprint-from-known-ingredients_100g'), "(per 100g)")

    proteins = product.get('nutriments').get('proteins')
    carbohydrates = product.get('nutriments').get('carbohydrates')
    sugars = product.get('nutriments').get('sugars')
    fat = product.get('nutriments').get('fat')
    carbon_footprint = product.get('nutriments').get('carbon-footprint-from-known-ingredients_100g')

    return {
        "ecoscore": ecoscore,
        "nutriscore": nutriscore,
        "proteins": proteins,
        "carbohydrates": carbohydrates,
        "sugars": sugars,
        "fat": fat,
        "carbon_footprint": carbon_footprint
    }


#Product = input("Which product are you looking for?\n")
#get_product_info(Product)