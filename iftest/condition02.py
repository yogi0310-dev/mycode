#!/usr/bin/env python3

hostname = input("what value should we set for hostname?")

print("Hostname is set to", hostname)
## Notice how the next line has changed
## her we use the str.lower() method to return to lowercase string

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config to the screen")

# Always Display to the user
print("Exiting the script")
