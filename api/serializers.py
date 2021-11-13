from rest_framework import serializers
from .models import Feeds

# this is basically used to convert the data to the json format
class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = "__all__" # this is for displaying all the feilds present in the Videos feild we can custmoze that also.