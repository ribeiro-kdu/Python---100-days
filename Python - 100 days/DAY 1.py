"""
_____________________
This code generates a Band Name in case the user finds it hard to think of a name for theirs.
It was made for the 100-day-coding Python challenge DAY1.
So, generate a name for your band, will you?
______________________
"""

#First, it welcomes the user:
print("Welcome to the Band Name Generator!\n")

#Second, it asks the user to enter a city name and saves it as a string variable called city_name.
city_name = input(str("What's the name of the city you grew up in?\n"))

#The line code below was previously used to make sure the generated variable was indeed a string one.
#print(type(city_name))

#Then, the user is asked for his pet's name, and it is saved in a string called pet_name.
pet_name = input(str("\nWhat's the name of your pet?\n"))

#The test is also done for that variable in the following line:
#print(type(pet_name))

#Last, the user is shown an idea of a name for their band:
print("\nThe name of your band could be: " + city_name + " " + pet_name + "...")
