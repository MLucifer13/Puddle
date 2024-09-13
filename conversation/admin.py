from django.contrib import admin

from .models import Conversation,ConvesationMessage

admin.site.register(Conversation)
admin.site.register(ConvesationMessage)