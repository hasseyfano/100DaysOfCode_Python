
    # Exercises
    # Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
    # Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
    # Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
    # Use an f-string to print the movie name and release year by accessing your new movie tuple.
    # Add the new movie tuple to the movies collection using append.
    # Print both movies in the movies collection.
    # Remove the first movie from movies. Use any method you like.
    
movies= ['(the legend of Zoro, Joe Doe, 2004, $430M)', 
         '(the mazer runner,Ben Ian, 2024, $110M)',
         '(dooms day, Stevie Wander , $680M)',
         '(the Traveller, Chris Hugh,  2014, $150M)'
                  
         ]
print (movies)

movieTitle=input("Enter movie title: ").strip()
directorName=input("Enter director name: ").strip().title()
releaseYear=input("Enter release year: ")
movieBudget=input("Enter the movie budget: ")

newMovie= (movieTitle , directorName ,releaseYear ,movieBudget).strip()
print(movies.append(newMovie))

# to remove from the last use pop() 
# to add to the list use append()
# to remove from any in the tuple remove ie movies.remove() or use del movies[2]
