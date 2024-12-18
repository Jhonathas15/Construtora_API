from django.contrib import admin
from django.urls import path, include
from card.views import CardListCreateView, CardRetriveUpdateDestroyView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # authentication
    path('api/stage/v1/', include('authentication.urls')),
    # card
    path('api/stage/v1/', include('card.urls')),
]
