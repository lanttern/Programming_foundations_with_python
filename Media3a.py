import webbrowser
class movie ():
    def __init__(self, movie_title, movie_storyline, movie_photo, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_photo
        self.trailer_youtube_url = movie_trailer
    def show_trail(self):
        webbrowser.open (self.trailer_youtube_url)
#    def show_review (self):
 #       webbrowser.open (self.review)
