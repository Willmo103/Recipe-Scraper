#! /bin/bash

echo "Creating virtual environment"
python -m virtualenv venv
echo "Activating virtual environment"
source venv/bin/activate
echo "installing requirements"
pip -r install requirements.txt
deactivate
echo "All requirements successfully installed"
echo "Run command 'python app.py' to run the scraper tool."
