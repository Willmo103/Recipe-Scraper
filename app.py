from scrapers import scrape_simply_quinoa
import os
from utils import write_json as wj

# The list of URLs to be scraped
recipe_urls = []

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

num_of_recipes = len(recipe_urls)
for i in range(num_of_recipes):
    url = recipe_urls[i]
    print(f"\nWriting {i+1} of {num_of_recipes} recipes...")
    json_data = scrape_simply_quinoa(url)
    wj(file_path, json_data)
