from scrapers import (
    scrape_myRecipes,
    scrape_real_food_dietitians,
    scrape_simply_quinoa,
    scrape_simply_recipes,
    scrape_allRecipes,
)
import os
from utils import write_json as wj

# The list of URLs to be scraped
recipe_urls = []

# objects to hold data on websites supported
SUPPORTED_WEBSITES = [
    {
        "name": "AllRecipes",
        "url": "https://www.allrecipes.com",
        "scraper": scrape_allRecipes,
    },
    {
        "name": "MY Recipes",
        "url": "https://www.myrecipes.com",
        "scraper": scrape_myRecipes,
    },
    {
        "name": "Simply Recipes",
        "url": "https://www.simplyrecipes.com",
        "scraper": scrape_simply_recipes,
    },
    {
        "name": "Simply Quinoa",
        "url": "https://www.simplyquinoa.com",
        "scraper": scrape_simply_quinoa,
    },
    {
        "name": "The Real Food Dietitians",
        "url": "https://therealfooddietitians.com",
        "scraper": scrape_real_food_dietitians,
    },
]

# variable of the users choice of website
website_choice = ""

# First we will query the user for their root output
# folder to save our .json files from each webpage
print("Please enter the filepath where the recipes.json files should be saved")
file_path = input("Filepath?\n> ")

# validate that the path provided will actually work
# or else this will break when it goes to save the .json files
while not os.path.exists(file_path):
    print(
        "Invalid or broken path! \n\nPlease enter the filepath where the recipes.json files should be saved"
    )
    file_path = input("Filepath?\n> ")

# Since were going to create a folder to hold our output files
# inside of the users root directory we have to check that our
#  output folder there already, or create one if its not.
if not os.path.exists(f"{file_path}/recipes-json"):
    os.mkdir(f"{file_path}/recipes-json")
    file_path = file_path + "/recipes-json"
    print("Created folder '/recipes-json'.")
else:
    file_path = file_path + "/recipes-json"
    print("Output folder found!")

# let the user know where they will be able to locate the json files.
print(f"The output recipes can be found at {file_path}")

# Get user's choice of website of the websites currently supported
print("These are the currently supported websites.\nEnter Any url form these sites:\n")
i = 0
for site in SUPPORTED_WEBSITES:
    i += 1
    print(f"{i} -- {site.get('name')} -- {site.get('url')}")
print("\n")

# Start the collection process. This block allows the user to enter
#  as many urls as they want to until they hit enter to proceed to
# scraping and saving the data
print("\nEnter URLs for recipes you want to scrape, or hit enter when finished.")
recipe = input("\nFirst URL?\n> ")
while recipe != "":
    # check to make sure each url is only added once
    # and let them know it has been successfully
    # added to the scraping list.
    if recipe not in recipe_urls:
        recipe_urls.append(recipe)
        print("Added!\n")
    else:
        print(f"URL '{recipe}' has already been added\n")
    recipe = input("Next URL?\n> ")

print("All data saved!\n")
print("\nRecipes:")
for i in range(len(recipe_urls)):
    print(f"{i + 1}) {recipe_urls[i]}")
print("Ready to beguin scraping data.")

# Use determine which scraper to use from each urls website
num_of_recipes = len(recipe_urls)
for i in range(num_of_recipes):
    url: str = recipe_urls[i]
    index = None
    for j in range(len(SUPPORTED_WEBSITES)):
        if url.startswith(SUPPORTED_WEBSITES[j].get("url")):
            print(f"\nWriting {i+1} of {num_of_recipes} recipes...")
            json_data = SUPPORTED_WEBSITES[j].get("scraper")(url)
            wj(file_path, json_data)
            break
