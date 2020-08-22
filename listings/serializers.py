from . import models
from rest_framework import serializers


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Listing
        fields = ['title', 'city']


class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Realtor
        fields = ['name']
