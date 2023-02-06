import spacy
import math

# Loading language model
nlp = spacy.load("en_core_web_md")

# movie that we are going to compare in order to give recommendation, so we include it in the model
planet_hulk = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,the Illuminati trick Hulk into a suttle and launch him into space to a planet where the Hulk can leave in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as gladiator.")

# list that will contain description of the movies
movies_description = []
# list that will contain movie names
movies = []

# openning text file:
try:
    with open("movies.txt", "r") as file:
    # splitting each line of text on movie name and movie description and adding elements to the corresponding lists
        for line in file:
            parts = line.strip().split(":")
            movies_description.append(parts[1])
            movies.append(parts[0])
except FileNotFoundError:
    print("Error: The file 'movies.txt' was not found. Please check the path and try again.")

# function that takes in description of the movie and outputs string as a recommendation of which movie user should watch next based on similarity with movies in the movie_description list
def similar_movie(description:str) -> str:
    # list that will contain similarity values
    similarities = []
    # iterating through movies description and adding each one to the model
    for movie in movies_description:
        movie = nlp(movie)
        # adding values to the list
        try:
            similarity = movie.similarity(description)
        except TypeError:
            print("Error: Objects are of different data types and cannot be compared.")
        similarities.append(similarity)
    # finding index for the most similar movie to the coparible movie description
    try:
        index = similarities.index(max(similarities))
    except ValueError: 
        print("Error: No similar movie was found. Please try again with a different description.")
    # finding name of the movie that is most siailar
    most_similar_movie = movies[index]
    # returning recommendation based on the comparison and providing description of the movie to watch
    return(f"Based on the \"Planet Hulk\", next movie we would reccomend you to watch is {most_similar_movie} and here is a short description:\n\n \"{movies_description[index]}\"")

# calling and printing the function
print(similar_movie(planet_hulk))


