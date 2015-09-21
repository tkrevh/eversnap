from django.contrib import admin
from tweetsalbum.models import Picture, TUser, Album

# Register models for use in admin backend
admin.site.register(Picture)
admin.site.register(TUser)
admin.site.register(Album)
