from rest_framework import serializers
from card.models import Card


class CardModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
