from django.shortcuts import render, redirect
import random

def render_home_page(request):
    print("You hit the home route!")
    return render(request, "landing.html")

def render_game_page(request):
    return render(request, "game.html")

def start_game(request):
    print("User submitted form!")
    print(request.POST)
    print(request.POST['username'])
    request.session['new_key']="new value"
    request.session['name']=request.POST['username']
    return redirect('/game_page')

def process_guess(request):
    print(request.POST)
    random_number = round(random.random()*10)
    if int(request.POST['guess']) == random_number:
        request.session['results']="YOU GUESSED THE NUMBER!"
    elif int(request.POST['guess'])>random_number:
        request.session['results']="You guessed too high!"
    else:
        request.session['results']="You guessed too low!"
    return redirect('/game_page')
