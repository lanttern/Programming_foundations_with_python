# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 17:43:29 2014

@author: zhihuixie
"""
import fresh_tomatoes
import Media3a

Frozen = Media3a.movie("Avatar", "A story about sisters", "http://flavorwire.files.wordpress.com/2013/11/frozen2.jpg", "https://www.youtube.com/watch?v=Fq00mCqBMY8")
Frozen1 = Media3a.movie("Avatar", "A story about sisters", "http://flavorwire.files.wordpress.com/2013/11/frozen2.jpg", "https://www.youtube.com/watch?v=Fq00mCqBMY8")
Frozen2 = Media3a.movie("Avatar", "A story about sisters", "http://flavorwire.files.wordpress.com/2013/11/frozen2.jpg", "hhttps://www.youtube.com/watch?v=Fq00mCqBMY8")
#print Frozen.title
#Frozen.show_trail()
movies = [Frozen, Frozen1, Frozen2]
#fresh_tomatoes.open_movies_page(movies)
print (Media3a.movie.__doc__)
print (Media3a.movie.__name__)
print (Media3a.movie.__module__)