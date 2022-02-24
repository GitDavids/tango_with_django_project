from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from game_of_life.models import Category, Page
# from game_of_life.forms import CategoryForm, PageForm, UserForm, UserProfileForm

from datetime import datetime


# Main page
def index(request):
    context_dict = {}

    return render(request, 'game_of_life/index.html', context=context_dict) # TODO


# Account pages
def user_login(request):
    context_dict = {}

    return render(request, 'game_of_life/login.html', context=context_dict) # TODO

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('game_of_life:index'))

def register(request):
    context_dict = {}

    return render(request, 'game_of_life/register.html', context=context_dict) # TODO


# Miscellaneous pages
def game_logic(request):
    context_dict = {}

    return render(request, 'game_of_life/game_logic.html', context=context_dict) # TODO

def interesting_patterns(request):
    context_dict = {}

    return render(request, 'game_of_life/interesting_patterns.html', context=context_dict) # TODO

def about(request):
    context_dict = {}

    return render(request, 'game_of_life/about.html', context=context_dict) # TODO

def all_initial_states(request):
    context_dict = {}

    return render(request, 'game_of_life/all_initial_states.html', context=context_dict) # TODO


# User specific pages
def user_account(request, user_slug):
    context_dict = {}

    return render(request, 'game_of_life/REPLACE.html', context=context_dict) # TODO

def create_initial_state(request, user_slug):
    context_dict = {}

    return render(request, 'game_of_life/REPLACE.html', context=context_dict) # TODO

def user_initial_states(request, user_slug):
    context_dict = {}

    return render(request, 'game_of_life/REPLACE.html', context=context_dict) # TODO


# Specific state
def state(request, user_slug, state_name_slug):
    context_dict = {}

    return render(request, 'game_of_life/REPLACE.html', context=context_dict) # TODO


# Moderator page
def create_add_pattern(request):
    context_dict = {}

    return render(request, 'game_of_life/REPLACE.html', context=context_dict)# TODO



