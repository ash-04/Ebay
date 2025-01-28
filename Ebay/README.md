#Ebay search Suite

1. This ui suite allows you to run the UI search on Ebay of book basis based on the parameters - Browser, OS, Platform, Environment and item name i.e. book selected by the user.
2. The api suite test 3 TCs are per the requirements

How to run script

1. Check other necessary files are present in Resources:
    - config.py

2. Create a venv environment
Reference: https://docs.python.org/3/library/venv.html)
Install packages in the requirements through pip For Windows:
Run Command: pip install -r requirements.txt 
Run the script in the same venv on the terminal. To Run complete suite:
Command to run ui suite : python .\ui_executor.py Chrome Windows Desktop Prod "Book"
Command to run api suite : python .\api_executor.py

   
3. Supported Params for UI sanity:

    Browser (-bw)
    Chrome
    
    OS (-z)
    Windows
    
    Platform (-x)
    Desktop,
    
    environment(-t)
    Prod
    
    item name(-a)
    "Book"