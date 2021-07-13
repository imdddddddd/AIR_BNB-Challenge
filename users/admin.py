from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
  
  """Class Custom Admin"""

  list_filter = ("language","preference","favourite_movie_genre")
  fieldsets = UserAdmin.fieldsets +(
    (
      "Custom Profile",
      {
        "fields":(
          "bio",
          "preference",
          "language",
          "favourite_movie_genre"
        
       )
      },
    ),
  ) 