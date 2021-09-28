#!/usr/bin/env python3
ipchk = input("Apply an IP Address: ") # this line now prompts the user

ipchk = input("Please confirm IP Address: ") # this line will confirm IP address

# if user set IP of gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
    print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
    print("You did not provided input.") # indented under else
