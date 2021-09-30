#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com
   
   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/
   
   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

#import pretty print

import pprint

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()
   
    #print the data into a file

    with open(f"{setcode}_cards.set", "w") as rcfile:
        pprint.pprint(cards, stream=rcfile) # prints data prettier
        # print(cards, file=rcfile)

if __name__ == "__main__":
    main()

