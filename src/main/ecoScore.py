import openfoodfacts
import json
import re


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

    print("Proteins:", product.get('nutriments').get('proteins'), "g")
    print("Carbohydrates:", product.get('nutriments').get('carbohydrates'), "g")
    print("Sugar:", product.get('nutriments').get('sugars'), "g")
    print("Fat:", product.get('nutriments').get('fat'), "g")
    print("Carbon Footprint From Known Ingredients:", product.get('nutriments').get('carbon-footprint-from-known-ingredients_100g'), "(per 100g)")



Product = input("Which product are you looking for?\n")
get_product_info(Product)