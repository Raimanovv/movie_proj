from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 11
    actions = ['set_dollars', 'set_euro']

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?!'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновленно {count_updated} записей',
            messages.ERROR
        )

