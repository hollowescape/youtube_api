from django.db import models

# Create your models here.
class Feeds(models.Model):
    title = models.CharField(null=True,blank=True,max_length=300)           # Title Of the Video
    description = models.CharField(null=True, blank=True, max_length=4000)  # Description Of the Video
    publishingDateTime = models.DateTimeField()                             # Publish date/time Of the Video
    thumbnailsUrls = models.URLField()                                      # Url Of the Thumbnail
    channelTitle = models.CharField(null=True,blank=True,max_length=300)    # Title/Name Of the Channel