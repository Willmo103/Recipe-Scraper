import requests as r
from bs4 import BeautifulSoup as bs

# this import shows up as one we're not using, but we
# still have to have it installed for BeautifulSoup
# to make use of it
import html5lib


def scrapeSimplyQ(url: str) -> dict:
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
    ingredients = soup.find("div", class_="wprm-recipe-ingredients-container").getText()
    instructions = soup.find(
        "div", class_="wprm-recipe-instructions-container"
    ).getText()
    nutrition = soup.find("div", class_="wprm-nutrition-label-container").getText()
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

    # Eventually I plan on adding more sites to
    # be scrapped per the request of the person
    # this script is for, But presently this will
    # only work with SimplyQuinoa.com
