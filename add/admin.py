from django.contrib import admin
from add.models import Comment, Gossip

# Register your models here.
admin.site.register(Gossip)
admin.site.register(Comment)