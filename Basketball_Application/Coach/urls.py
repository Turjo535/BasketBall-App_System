
from django.urls import path
from .views import Team_Information_View,Team_Scouting_View,Team_Information_List_View,Team_Scouting_List_View
urlpatterns = [
    path('teaminfo/',Team_Information_View.as_view(),name="Team-Info"),
    path('scouting/',Team_Scouting_View.as_view(),name="Team_Scouting"),
    path('teams-list/',Team_Information_List_View.as_view(), name='Teams-List'),
    path('teams-scouting/',Team_Scouting_List_View.as_view(), name='Teams-Scouting'),
]
