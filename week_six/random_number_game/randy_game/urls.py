from django.urls import path
from . import views

urlpatterns=[
    path('', views.render_home_page),
    path('game_page', views.render_game_page),
    path('start_game', views.start_game),
    path('make_guess', views.process_guess)
]