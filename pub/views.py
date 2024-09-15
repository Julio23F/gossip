from django.shortcuts import render
from add.models import Comment, Gossip

# Create your views here.
def home(request):
    gossips = Gossip.objects.all()
    return render(request, "home.html", {"gossips" : gossips})


def comment(request, slug):
    gossip = Gossip.objects.get(slug = slug)
    comments = Comment.objects.filter(gossip = gossip)
    print(comments)
    if request.method == "POST":
        content = request.POST.get("content")
        comment = Comment(content = content, user = request.user, gossip = gossip)
        comment.save()
    return render(request, "comment.html", {"gossip" : gossip, "comments" : comments})