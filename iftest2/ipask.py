#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user to enter IP Address

ipchk = input("Please confirm IP Address: ") # this line will confirm the IP Address

# a provided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
    print("you did not provide input.") # indented under else
