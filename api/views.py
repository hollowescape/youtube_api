from django.shortcuts import render
from django.http import HttpResponse

from .get_feed import getnewfeeds
from .models import Feeds
from .serializers import FeedsSerializer

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def get_latest_feeds(request):
    try:
        getnewfeeds()
        return HttpResponse("Your videos has been refreshed. Go to the '/' url or Refresh Localhost to view added videos")
    except:
        return HttpResponse("Error encountered")

class FeedList(generics.ListAPIView):
    queryset = Feeds.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   
    # Adding the search and filter fields
    search_fields = ['title']
    filter_fields = ['channelTitle']

    # For sorting the videos data in reverse chronological order by default
    ordering = ['-publishingDateTime']
    serializer_class = FeedsSerializer
    pagination_class = PageNumberPagination