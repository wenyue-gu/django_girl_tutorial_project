from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Cats

# Create your views here.
def cat_home(request):
    return render(request, 'cats/cat_home.html', {})

def cat_list(request):
    #posts -> queryset
    posts = Cats.objects.all()
    return render(request, 'cats/cat_list.html', {'cats':cats})


def cat_detail(request, pk):
    cat = get_object_or_404(Cats, pk=pk)
    return render(request, 'cats/post_detail.html', {'cat': cat})