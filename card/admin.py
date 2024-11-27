from django.contrib import admin
from card.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ('id', 'information', 'location',)
    list_display = ('id', 'information', 'location',)
