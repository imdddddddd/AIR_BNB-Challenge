from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  
  """Class Custom User"""
  HERO = "hero"
  MARVEL = "marvel"
  HORROR = "horror"
  ADULT = "19"
  BOOK =  "book"
  MOVIE = "movie"
  LANGUAGE_ENG = "EN"
  LANGUAGE_KOR = "KR"

  LANGUAGE_CHOICES = (
      (LANGUAGE_ENG, "ENG"),
      (LANGUAGE_KOR, "KOR"),
  )

  CHOICES_GENRE = [
    (HERO, "HERO"),(MARVEL,"MARVEL"),(HORROR,"HORROR"),(ADULT,"19")
  ]
  CHOICES_PREFERENCE = [
    (BOOK, "BOOK"), (MOVIE,"MOVIE")    
  ]


  bio = models.TextField(blank=True, null=True)
  preference = models.CharField(max_length=5,blank=True, null=True, choices=CHOICES_PREFERENCE)
  language = models.CharField(max_length =3, blank=True,null=True,choices = LANGUAGE_CHOICES)
  favourite_movie_genre = models.CharField(blank=True, null=True, max_length = 8,choices= CHOICES_GENRE )
  

