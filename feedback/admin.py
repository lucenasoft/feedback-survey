from django.contrib import admin

from .models import Feedbacks

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'message']
