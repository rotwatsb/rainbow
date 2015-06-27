from django.contrib import admin
from comments.models import Conversation, Comment


class ConversationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Comment)
