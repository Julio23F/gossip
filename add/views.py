from django.shortcuts import render, redirect
from django.http import HttpResponse
from add.models import Gossip

# Create your views here.
def add_gossip(request):
    if request.method == 'POST':
        title = request.POST.get('titre')
        content = request.POST.get('contenu')
        gossip = Gossip(
            title=title,
            content=content,
            user=request.user,
            slug=title.replace(' ', '-').lower()
        )
        gossip.save()
        return redirect("home")

    
    return render(request, "index.html")
