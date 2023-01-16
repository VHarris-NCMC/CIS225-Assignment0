# Assignment0.py -- Victor Harris 
# Write a program that asks for a user's first and last name. 
# If user does NOT exist, ask user for their top 5 favorite movies
# with the following data points: User's first & last name, movie title, director, year released, IMDB start rating, Rotten Tomatoes star rating, and MPAA rating.
# If user DOES exist, display their movie data. 


# import constants
import Constants


## Ask for user's first and last name
users = []

class User:                                 ## The assignment description said class objects were not expected, but it seemed illogical to write this program without them. 
    
    def __init__(self, firstName, lastName):

        self.name = firstName, lastName                                     ## tuple for storing the user's name
        self.favorites = self.GetFavoriteMovies(Constants.moviesRequired)   ## list of user's favorite movies, requesting during instantiation
        self.isNew = True                                                   ## Sets the user as new during instantiation, to be set to false the first time the user is found during user lookup
    
    def GetFavoriteMovies(self, nOfmovies):         
        
        movies = []                                                         ## local movies list initialized
        
        print("What are your top", nOfmovies,  "favorite movies? \n")       ## output to request favorite movies
            
        i = 0                                                               ## incrementer initialization
        while i < nOfmovies:
            
            titleInput = input("What is the title of your " + Constants.ranks[i] + " favorite movie? ") ## request from user name of favorite movie
            movie = Movie(titleInput)                                       ## instantiate movie with title as argument
            movies.append(movie)                                            ## Append new movie to list local list of movies
            i = i+1

        return movies                                                       ## return local list as user's favorites

    
    def PrintUserFavorites(self):                                           ## prints each of the user's favorite movies

        username = self.name[0]+ ' ' + self.name[1]
        print(username + '\'s favorite movies:')                            ## convert name tuple to string for printing
        for movie in self.favorites:
            
            ## print movie details: 
            print(movie.title)                                                  
            print('MPAA Rating: ' + Constants.MPAAratings[movie.rating_MPAA])
            print(Constants.IMDBRatings[movie.rating_IMDB] + ' On IMDB')
            print(Constants.RottenTomatoRatings[movie.rating_RottenTomatoes] + ' On Rotten Tomatoes')


class Movie: 

    def __init__(self, titleInput):
        self.title = titleInput             ## use title parameter to name movie in constructor
        
        ## request ratings from user
        self.rating_MPAA = self.GetRating(Constants.MPAAratings, 'What is this movie\'s MPAA rating? ')    
        self.rating_IMDB = self.GetRating(Constants.IMDBRatings, 'What is this movie\'s rating on IMDB? ')
        self.rating_RottenTomatoes = self.GetRating(Constants.RottenTomatoRatings, 'What is this movie\'s rating on Rotten Tomatoes? ')
    
    def GetRating(self, ratings, question):
        rating = None                       ## initialize rating
        while rating == None:

            
            print(question + "\n")                  ## out question argument to prompt user input
            i = 0
            for rating in ratings:                  ## iterate through ratings list argument
                print(i, " - ", rating, end = " ")  ## iterate through available ratings 
                i = i+1
                if i%3 == 0:
                    print('\n')
                  
            print("\n")

            
            userInput = input()                     ## save input as string

            try:
                rating =  int(userInput)            ## try converting input to int
            except ValueError:
                "Invalid input"
        return rating                               ## return rating as int
    
def GetUser():
    ## prompt user for first / last name, save as local values
    firstName = input("Please enter your first name :")     
    lastName = input("Please enter your last name :")

    
    for user in users:                                          ## iterate through user list to search for matching name
        
        if type(user) is not User:                              ## if, for some reason a (because python), an object in user list is not a User class object, skip entry 
            continue
        
        if firstName == user.name[0] and lastName == user.name[1]:
            user.isNew = False                                 ## if user is found, they are no longer 'new'
            return user                                        ## return existing user
            
    user = User(firstName, lastName)                           ## if user is not found, instantiate a new one
    users.append(user)                                         ## add new user to user list
    return user                                                ## return new user 

def main():

    while(True):                                               ## run until closed
        user = GetUser()                                       ## search for user in user list, or create a new one (which requires the user to input their favorite movies)

        if not user.isNew:                                     ## user was found in user list, print their favorites. 
        
            user.PrintUserFavorites()

main()
