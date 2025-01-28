# Ebay search Suite

-This ui suite allows you to run the UI search on Ebay of book basis based on the parameters - Browser, OS, Platform, Environment and item name i.e. book selected by the user.
- The api suite test 3 TCs are per the requirements

# How to run script

# Check other necessary files are present in Resources:
- config.py
# Create a venv environment Reference: https://docs.python.org/3/library/venv.html) Install packages in the requirements through pip For Windows: Run Command: pip install -r requirements.txt 
- Run the script in the same venv on the terminal.
- To Run complete suite:
- Command to run ui suite : python .\ui_executor.py Chrome Windows Desktop Prod "Book"
- Command to run api suite : python .\api_executor.py

# Supported Params for UI sanity:

- Browser (-bw) Chrome
  
- OS (-z) Windows

- Platform (-x) Desktop,

- Environment(-t) Prod

- item name(-a) "Book"
