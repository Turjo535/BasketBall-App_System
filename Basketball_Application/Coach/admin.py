from django.contrib import admin
from .models import Team_Information_model, Team_Scouting_model

class Team_Information_Admin(admin.ModelAdmin):
    list_display=[field.name for field in Team_Information_model._meta.fields]
class Scouting_Admin(admin.ModelAdmin):
    list_display=[field.name for field in Team_Scouting_model._meta.fields]




admin.site.register(Team_Information_model,Team_Information_Admin)
admin.site.register(Team_Scouting_model,Scouting_Admin)
