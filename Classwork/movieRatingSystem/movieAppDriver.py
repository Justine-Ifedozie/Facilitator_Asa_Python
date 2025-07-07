from movieRatingSystem import add_movie, find_a_movie

is_running = True
while is_running:
    welcome_text = """
Welcome to Movie Rating System!
_______________________
You will be required to
make a selection:
1. Add a movie
2. Rate a movie
3. View average ratings
4. Exit
_______________________
                                """
    print(welcome_text)

    user_choice = int(input("Make a selection between 1 - 4: "))
    match user_choice:
        case 1:
            movie_name = input("Enter movie name: ")
            add_movie(movie_name)
        case 2:
            movie_name = input("Enter movie name to rate it: ")

        case 3:
            movie_name = input("Enter movie name to rate it: ")
        case 4:
            is_running = False
        case _:
            print("Invalid input")

print("Thank you! Have a nice day!")