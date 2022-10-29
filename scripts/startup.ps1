Write-Output "Creating virtual environment."
python -m virtualenv venv
Write-Output "Activating virtual environment."
venv/Scripts/activate
Write-Output "Installing required dependancies."
pip install -r rquirements.txt
Write-Output "Deactivating virtual environment."
deactivate
Write-Output "All requirements installed, ready to scrape."
Write-Output "run command 'python app.py' to run scraper tool"
