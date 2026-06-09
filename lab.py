class MovieWatchlist:
    def __init__(self):
        self.__movies=[]

    def addMovie(self,title,genre,rating):
        movie={
            "title":title,
            "genre":genre,
            "rating":rating

        }
        self.__movies.append(movie)
        print(title, "has been added to your watchlist!")

    def displayMovies(self):
        if len(self.__movies)==0:
            print("no movies found")
        else:
            print("Movie watchlist")
            print("=================")

            for movie in self.__movies:
                print("title:", movie["title"])
                print("genre:", movie["genre"])
                print("rating:", movie["rating"])
                print("========================")

    def searchMovie(self,title):
        for movie in self.__movies:
            print("movie found!")
            print("title:", movie["title"])
            print("genre:", movie["genre"])
            print("rating:", movie["rating"])
            print("========================")
            return
        print("movie not found")

    def countMovies(self):
        return len(self.__movies)

watchlist=MovieWatchlist()
number_of_movies=int(input("How many movies you want to add? Please enter a valid number:"))

for i in range(number_of_movies):
    print("Enter movie",i+1)

    title=input("enter movie title:")
    genre=input("enter movie genre:")
    rating=float(input("enter movie rating out of 10:"))

    watchlist.addMovie(title,genre,rating)

watchlist.displayMovies()

searchTitle=input("search movies:")
watchlist.searchMovie(searchTitle)
print("total movies:",watchlist.countMovies())