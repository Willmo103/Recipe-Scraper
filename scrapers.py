from dis import Instruction
import requests as r
from bs4 import BeautifulSoup as bs
from utils import remove_blank_lines, remove_ingredients

# this import shows up as one we're not using, but we
# still have to have it installed for BeautifulSoup
# to make use of it
import html5lib


def scrape_simply_quinoa(url: str) -> dict:
    # Send a request for the url.
    req = r.request("get", url).text

    # parse the returned html of the page with BeautifulSoup
    soup = bs(req, "html5lib")

    # get all of the items to populate our json file
    name = soup.find("h2", class_="wprm-recipe-name").getText()
    summary = soup.find("div", class_="wprm-recipe-summary").getText()
    prep_time = soup.find("div", class_="wprm-recipe-prep-time-container").getText()
    cook_time = soup.find("div", class_="wprm-recipe-cook-time-container").getText()
    servings = soup.find("div", class_="wprm-recipe-servings-container").getText()
    calories = soup.find("div", class_="wprm-recipe-calories-container").getText()
    nutrition = soup.find("div", class_="wprm-nutrition-label-container").getText()

    # get each ingredient div
    ingredients_raw = soup.findAll("li", class_="wprm-recipe-ingredient")

    # create a list of ingredients
    ingredients = []
    for ingredient in ingredients_raw:
        item = ingredient.getText()
        ingredients.append(item)

    # get each instruction div
    instructions_raw = soup.findAll("div", class_="wprm-recipe-instruction-text")

    # create a list of instructions
    instructions = []
    for item in instructions_raw:
        line = item.getText()
        instructions.append(line)

    # not all of the recipes on this site will have a note field
    # so we need to do some checking
    notes = soup.find("div", class_="wprm-recipe-notes-container")

    # Added this bit to determine if theirs notes to be found
    if notes:
        notes = notes.getText()
    else:
        notes = None

    # create our json schema and return it to be written
    recipeJson = {
        "name": name,
        "summary": summary,
        "prep_time": prep_time,
        "cook_time": cook_time,
        "servings": servings,
        "calories": calories,
        "ingredients": ingredients,
        "instructions": instructions,
        "notes": notes,
        "nutrition": nutrition,
    }
    return recipeJson


def scrape_real_foodie_titans(url: str) -> dict:
    req = r.request("get", url).text

    soup = bs(req, "html5lib")

    name = soup.find("h2", "tasty-recipes-title").getText()
    prep_time = soup.find("span", "prep-time").getText()
    cook_time = soup.find("span", "cook-time").getText()
    servings = soup.find("span", class_="yield").getText()
    ingredients_raw = soup.find("div", class_="tasty-recipes-ingredients").getText()
    ingredients = remove_ingredients(ingredients_raw).replace("Ingredients", "").strip()
    instructions_raw = soup.find("div", class_="tasty-recipes-instructions").getText()
    instructions = (
        remove_blank_lines(instructions_raw).replace("Instructions", "")
    ).strip()
    print(ingredients)
    print("\n\n")
    print(instructions)
    ...


# scrape_real_foodie_titans(
#     "https://therealfooddietitians.com/breakfast-pizza-with-hash-brown-crust/"
# )

scrape_simply_quinoa(
    "https://www.simplyquinoa.com/quinoa-stuffed-eggplant-with-tahini-sauce/"
)
# Eventually I plan on adding more sites to
# be scrapped per the request of the person
# this script is for, But presently this will
# only work with SimplyQuinoa.com
