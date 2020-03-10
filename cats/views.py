from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cats

# Create your views here.
def cat_home(request):
    return render(request, 'cats/cat_home.html', {})

def cat_list(request):
    #cats -> queryset
    cats = Cats.objects.all()
    return render(request, 'cats/cat_list.html', {'cats':cats})


def cat_detail(request, pk):
    cat = get_object_or_404(Cats, pk=pk)
    cat.time()
    return render(request, 'cats/cat_detail.html', {'cat': cat})

def cat_interact(request, pk, action):
    cat = get_object_or_404(Cats, pk=pk)
    play = False
    pet = False
    feed = False
    if(action == 1):
        cat.play()
        play = True
    elif(action ==2):
        cat.pet()
        pet = True
    elif(action==3):
        cat.feed()
        feed = True
    return render(request, 'cats/cat_interact.html', {'cat': cat, 'play': play, 'feed':feed, 'pet':pet})