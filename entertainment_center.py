import fresh_tomatoes
import media

#instances of class Movie that define the instance variables

dbz_broly = media.Movie("Dragon Ball Super: Broly",
					 	"A lost Saiyan warrior could destroy the Universe",
					 	"https://upload.wikimedia.org/wikipedia/en/1/13/DB_THE_MOVIE_NO._20.jpg",
					 	"https://www.youtube.com/watch?v=hgTH0bZysYw")


toy_story = media.Movie("Toy Story 4",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/7/78/Toy_Story_4_teaser_poster.jpg",
						"https://www.youtube.com/watch?v=2DRD4xSUbhM")
#print(avatar.storyline)
#avatar.show_trailer()
venom = media.Movie("Venom",
					"A reporter 'Eddy Brock' and an alien symbiote save the world",
					"https://upload.wikimedia.org/wikipedia/en/1/18/Venom_%282018_film_poster%29.png",
					"https://www.youtube.com/watch?v=xLCn88bfW1o")

avengers = media.Movie("Avengers: Endgame",
					   "The surviving Avengers work to undo the damage done by Thanos",
					   "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
					   "https://www.youtube.com/watch?v=hVSpac8wx3I")

aquaman = media.Movie("Aquaman",
					  "Dis boi swim wit dem fish",
					  "https://upload.wikimedia.org/wikipedia/en/3/3a/Aquaman_poster.jpg",
					  "https://www.youtube.com/watch?v=WDkg3h8PCVU")

bohemiam_rhapsody = media.Movie("Bohemiam Rhapsody",
						   		"The story of the british rock band Queen",
						   		"https://upload.wikimedia.org/wikipedia/en/2/2e/Bohemian_Rhapsody_poster.png",
						  		"https://www.youtube.com/watch?v=mP0VHJYFOAU")

movies = [dbz_broly, toy_story, venom, avengers, aquaman, bohemiam_rhapsody]
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie__module__)