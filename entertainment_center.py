import media
import fresh_tomatoes


# Toy Story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://wwww.youtube.com/watch?v=vwyZH85NQC4"
    )

# Avatar movie: movie title, storyline, poster image and movie trailer
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://yutube.com/watch?v=-9ceBgWV8io"
    )

# School of Rock movie: movie title, storyline, poster image and movie trailer
school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
    )

# Kongfu Panda 3 movie: movie title, storyline, poster image and movie trailer
kongfu_panda_3 = media.Movie(
    "Kongfu Panda 3",
    "Panda Po learns kongfu and battles evil enemy",
    "https://upload.wikimedia.org/wikipedia/commons/a/a2/Kongfu-panda3.jpg",  # NOQA
    "https://www.youtube.com/watch?v=10r9ozshGVE"
    )

# Midnight in Paris movie:
# movie title, storyline, poster image and movie trailer
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=atLq2wQQsvU"
    )

# Hunger Games movie: movie title, storyline, poster image and movie trailer
hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PbA63a7H0bo"
    )

# Set the movies that will be passed to the media file
movies = [
    toy_story, avatar, school_of_rock,
    kongfu_panda_3, midnight_in_paris,
    hunger_games
    ]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
