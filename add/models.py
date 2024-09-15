from django.db import models
from accounts.views import User
from gossip.settings import AUTH_USER_MODEL

# Create your models here.
class Gossip(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()
    
    def __str__(self):
        return f"{self.title} publié par {self.user}"


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gossip = models.ForeignKey(Gossip, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gossip} : {self.content} commenté par {self.user}"

