from dis import Instruction
import requests as r
from bs4 import BeautifulSoup as bs
from utils import remove_blank_lines, list_from_str
import re

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
    prep_time = (
        soup.find("div", class_="wprm-recipe-prep-time-container")
        .getText()
        .replace("Prep Time", "")
        .strip()
    )

    # some small meals don't have a cook time field so we have to check that
    cook_time = soup.find("div", class_="wprm-recipe-cook-time-container")
    if cook_time:
        cook_time = cook_time.getText().replace("Cook Time", "").strip()
    else:
        cook_time = None

    servings = (
        soup.find("div", class_="wprm-recipe-servings-container")
        .getText()
        .replace("Servings", "")
        .replace("servings", "")
        .strip()
    )
    calories = (
        soup.find("div", class_="wprm-recipe-calories-container")
        .getText()
        .replace("Calories", "")
        .strip()
    )
    nutrition_raw = soup.find("div", class_="wprm-nutrition-label-container").getText()
    nutrition = nutrition_raw.split(" | ")

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
        "prepTime": prep_time,
        "cookTime": cook_time,
        "servings": servings,
        "calories": calories,
        "ingredients": ingredients,
        "instructions": instructions,
        "notes": notes,
        "nutrition": nutrition,
    }
    return recipeJson


def scrape_real_food_dietitians(url: str) -> dict:
    req = r.request("get", url).text
    soup = bs(req, "html5lib")
    name = soup.find("h2", "tasty-recipes-title").getText()
    cook_time = soup.find("span", "cook-time").getText().replace("Cook: ", "")

    # Not all the recipes on this site have descriptions so we have to check
    summary = soup.find("div", class_="tasty-recipe-description")
    if summary:
        summary = summary.getText()
    else:
        summary = None

    prep_time = soup.find("span", "prep-time").getText().replace("Prep: ", "")
    servings = (
        soup.find("span", class_="yield")
        .getText()
        .replace("Servings: ", "")
        .replace("servings", "")
        .replace(" 1x", "")
    )

    # calories will get filled by data from the nutrition tags
    calories = ""

    # get and scrub the block text from the ingredients div
    ingredients_raw = (
        soup.find("div", class_="tasty-recipes-ingredients")
        .getText()
        .replace("Ingredients", "")
        .strip()
    )

    # create a list from the block text
    ingredients = list_from_str(ingredients_raw)

    # get and scrub the block text from instructions div
    instructions_raw = soup.find("div", class_="tasty-recipes-instructions").getText()
    instructions_raw = (
        remove_blank_lines(instructions_raw).replace("Instructions", "")
    ).strip()

    # create a list from block text
    instructions = list_from_str(instructions_raw)

    # get the nutrition data
    nutrition_raw = soup.find("div", class_="tasty-recipes-nutrition")

    # make a list of nutrition tags
    data_val = ""
    nutrition = []
    for value_tag in nutrition_raw.descendants:
        text = value_tag.getText()
        if re.match("[(a-zA-Z0-9]+: ", text):
            if text.startswith("("):
                text = text.replace("(", "")
            elif text.endswith(")"):
                text = text.replace(")", "")
            elif text.startswith("Calories: "):
                calories = text.split(":")[1]
            nutrition.append(text)
        data_val += value_tag.getText()

    notes = soup.find("div", class_="tasty-recipes-notes")
    if notes:
        notes = notes.getText().split("Notes")[1].strip()
    else:
        notes = None

    recipeJson = {
        "name": name,
        "summary": summary,
        "prepTime": prep_time,
        "cookTime": cook_time,
        "servings": servings,
        "calories": calories,
        "ingredients": ingredients,
        "instructions": instructions,
        "notes": notes,
        "nutrition": nutrition,
    }
    return recipeJson


# Eventually I plan on adding more sites to
# be scrapped per the request of the person
# this script is for, But presently this will
# only work with SimplyQuinoa.com
