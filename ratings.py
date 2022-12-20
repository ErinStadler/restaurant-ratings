"""Restaurant rating lister."""

import random
# put your code here

#define function here:
def read_restaurant_ratings(filename):
    
    #generate dictionary for storing information
    #open file
    restaurant_scores = {}
    data = open(filename)
    
    
    #step 1
    #loop through each line in the file
    for line in data:
        line = line.rstrip()
        line_lst = line.split(":")
        restaurant_scores[line_lst[0]] = line_lst[1]
    #prompt user input after for loop 
    
    user_restaurant = input("(enter '0' to exit) What is your restaurant name? ")
    if user_restaurant != '0': 
        # if user_score != '0':
        while True:
            try: 
                user_score = int(input("(enter '0' to exit) What is the restaurant rating from 1 to 5? "))
                if user_score in range (1, 6):
                    break
                else:
                    print("The number you input is not between 1 and 5. Try again")
            except: 
                print("Please type in a number!")

    # user_score = int(input("(enter '0' to exit) What is the restaurant rating from 1 to 5? "))
    # if user_score > 5 or user_score < 1:
    #    raise Exception("Sorry, no numbers below 1 or above 5.")
        restaurant_scores[user_restaurant] = int(user_score)
    

    # if user_restaurant == 0:
    #     del restaurant_scores[user_restaurant]
    #sort
     #if restaurant == "q" or score =="q": skip input stage
    #step 3: sort alphabetical order sort dictionary (return sorted() copy?)
    
    restaurant_scores = sorted(restaurant_scores.items())
    #print after sorted?
    # dict_items = restaurant_scores.items()
    for restaurant, rating in restaurant_scores:
        print(f"{restaurant} is rated at {rating}.")
        
    return restaurant_scores

print(read_restaurant_ratings("scores.txt"))
    
    #step 2
        #dictionary.items() = splits (restaurant, rating) into tuples
    #ask for input for new restaurant(key) with score (value)
    #add variables to dictionary if present q skips step entirely
       
    #file.close()?

#call function with files:
