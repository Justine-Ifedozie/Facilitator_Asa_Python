movie_app = []

def add_movie(movie_name, rating= ""):
    movie = [movie_name, rating]
    movie_app.append(movie)
    return movie_app

def find_a_movie(movie_name):
    for movie in movie_app:
        if movie[0] == movie_name:
            return movie
    return None

def rate_a_movie(movie_name, rating):
    for movie in movie_app:
        if movie[0] == movie_name:
            movie[1] = rating
            return movie
    return None

