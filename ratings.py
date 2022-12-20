"""Restaurant rating lister."""


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
    if user_restaurant is not '0': 
        user_score = input("(enter '0' to exit) What is the restaurant rating? ")
        if user_score is not '0':
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


