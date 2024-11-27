from django.urls import path
from . import views

urlpatterns = [
    path('card/', views.CardListCreateView.as_view(), name='card_list_create'),
    path('card/<int:id>', views.CardRetriveUpdateDestroyView.as_view(), name='card_retrive_update_destroy'),
]
