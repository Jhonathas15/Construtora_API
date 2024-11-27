from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from card.serializers import CardModelSerializer
from card.models import Card


class CardListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = Card.objects.all()
    serializer_class = CardModelSerializer


class CardRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = Card.objects.all()
    serializer_class = CardModelSerializer
