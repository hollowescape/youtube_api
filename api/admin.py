from django.contrib import admin

from .models import Feeds
# Register your models here.

#Here we are registering our model and then we will be making the migrations
admin.site.register(Feeds)