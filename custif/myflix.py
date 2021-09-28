#!/usr/bin/env python3

# this is list of Movies Available

Movies = ["1.Harry Potter","2.Mission Impossible","3.Transformers","4.Matrix","5.GodFather"]

print("1. Harry Potter")
print("2. Mission Impossible")
print("3. Transformers")
print("4. Matrix")
print("5. GodFather")

message = 'The movie is about to begin is '

# wrap connection in a float() to accept decimals as numbers
movie = float(input("Which movie you would like to see?"))
# if input value was higher or equal to 25
if movie == 1:
    message = message + ' Harry Potter '
elif movie == 2:
    message = message + ' Mission Impossible '
elif movie == 3:
    message = message + ' Transformers '
elif movie == 4:
    message = message + 'Matrix '
elif movie == 5:
    message == message + ' GodFather '
else:
    message = ' Please enter 1 - 5 '
print(message)

