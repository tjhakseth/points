from django.contrib import admin

from .models import Team, User, Points
# Register your models here.

admin.site.register(Team)
admin.site.register(User)
admin.site.register(Points)
