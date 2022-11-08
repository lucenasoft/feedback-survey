from django.contrib import admin

from .models import Feedbacks

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'message']
    list_display_links = ['author', 'email']
    search_fields = ['author', 'email']
    list_filter = ['author', 'email']
