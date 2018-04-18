import media
import fresh_tomatoes

# Here we create six Movie objects to display on the HTML page.
# The parameters are movie_title, movie_storyline, poster_image, trailer_youtube):

superbad = media.Movie("Superbad", "High-school seniors Seth (Jonah Hill) and Evan (Michael Cera) have high hopes for "
                                   "a graduation party: The co-dependent teens plan to score booze and babes so they "
                                   "can become part of the in-crowd, but separation anxiety and two bored police "
                                   "officers (Bill Hader, Seth Rogen) complicate the pair's self-proclaimed mission.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png",
                       "https://youtu.be/q3UFV1in5Qk")

black_dynamite = media.Movie("Black Dynamite", "After 'The Man' kills his brother and poisons the neighborhood with "
                                               "tainted liquor, a kung fu fighter (Michael Jai White) wages a war that "
                                               "takes him all the way to Nixon's White House.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Black_dynamite_poster.jpg/220px-Black_dynamite_poster.jpg",  # NOQA
                             "https://youtu.be/96Y24a0cyCE")

lost_translation = media.Movie("Lost in Translation", "A lonely, aging movie star named Bob Harris (Bill Murray) and a "
                                                      "conflicted newlywed, Charlotte (Scarlett Johansson), meet in "
                                                      "Tokyo. Bob is there to film a Japanese whiskey commercial; "
                                                      "Charlotte is accompanying her celebrity-photographer husband. "
                                                      "Strangers in a foreign land, the two find escape, distraction "
                                                      "and understanding amidst the bright Tokyo lights after a chance "
                                                      "meeting in the quiet lull of the hotel bar. They form a bond "
                                                      "that is as unlikely as it is heartfelt and meaningful.",
                               "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
                               "https://youtu.be/W6iVPCRflQM")

wind_rises = media.Movie("The Wind Rises", "A lifelong love of flight inspires Japanese aviation engineer Jiro "
                                           "Horikoshi (Hideaki Anno), whose storied career includes the creation of "
                                           "the A6M World War II fighter plane.",
                         "https://upload.wikimedia.org/wikipedia/en/a/a3/Kaze_Tachinu_poster.jpg",
                         "https://youtu.be/2QFBZgAZx7g")

namesake = media.Movie("The Namesake", "After moving from Calcutta to New York, members of the Ganguli family maintain "
                                       "a delicate balancing act between honoring the traditions of their native India "
                                       "and blending into American culture. Although parents Ashoke (Irrfan Khan) and "
                                       "Ashima (Tabu) are proud of the sacrifices they make to give their offspring "
                                       "opportunities, their son Gogol (Kal Penn) strives to forge his own identity "
                                       "without forgetting his heritage.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/The_Namesake.jpg",
                       "https://youtu.be/_sOaA-4Y8tI")

gangs_new_york = media.Movie("Gangs of New York", "Amsterdam Vallon (Leonardo DiCaprio) is a young Irish immigrant "
                                                  "released from prison. He returns to the Five Points seeking revenge "
                                                  "against his father's killer, William Cutting (Daniel Day-Lewis), "
                                                  "a powerful anti-immigrant gang leader. He knows that revenge can "
                                                  "only be attained by infiltrating Cutting's inner circle. Amsterda"
                                                  "m's journey becomes a fight for personal survival and to find a "
                                                  "place for the Irish people in 1860's New York.",
                             "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",
                             "https://www.youtube.com/watch?v=1bjh979vVG0")

# Creates a list of all of the objects created, then calls the function from fresh_tomatoes that will open the
# list of movies in an HTML page called Fresh Tomatoes

movies = [superbad, black_dynamite, lost_translation, wind_rises, namesake, gangs_new_york]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
