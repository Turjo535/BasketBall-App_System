from rest_framework import serializers
from .models import Player, Scouting_Context,Report_Model
from UserAccount.models import User

class Player_Information_Serializers(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    class Meta:
        model = Player
        fields = ['user',
            'jersey',
            'height',
            'position',
            'class_year',
            'game_context',
            'team',
            'gender',
            'opponent',
            'performance_note',
            'tournament',
            'image',
            'game_video',
            ]
class Player_list_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name', 'email', 'phone']

class Report_Serializers(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    class Meta:
        model=Report_Model
        fields=[
            'user',
            'title',
            'overview',
            'strength',
            'weaknesses', 
            'projection',
            'points_per_game', 
            'field_goal_percentage',
            'rebounds',
            'assists',
            'steals_and_blocks',
            ]
        
class Scouting_Context_Serializers(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    class Meta:
        model=Scouting_Context
        fields=[
            'user',
            'tournament_name',
            'game_result',
            'opponent_faced', 
            'score_or_margin',
            'game_flow_details', 
            ]
        

class ReportSerializerID(serializers.ModelSerializer):
    class Meta:
        model = Report_Model
        exclude = ['pdf'] 