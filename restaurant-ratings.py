# your code goes here
import sys

filename = sys.argv[1]
ratings_dictionary = {}
for list_of_restaurant in open(filename): # this pulls data from the file
	list_of_restaurant = list_of_restaurant.rstrip() # this strips the \n from the end of the line
	restaurant_name, ratings = list_of_restaurant.split(":") # this splits the line by the colon :
	ratings_dictionary[restaurant_name] = ratings # this assigns the split to a list 


for restaurant_name, ratings in sorted(ratings_dictionary.items()): # alphabetize the dictionary
	print "{} is rated at {}.".format(restaurant_name, ratings)

# list_of_keys = []
# list_of_keys.sort()
# for restaurant_name in list_of_keys:
# 	print restaurant_name and score_in_dictionary_in_scores.txt