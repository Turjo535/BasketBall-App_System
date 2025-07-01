from rest_framework import serializers
from .models import Team_Information_model, Team_Scouting_model
from UserAccount.models import User


class Team_Information_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    class Meta:
        model=Team_Information_model
        fields='__all__'

class Team_Scouting_Serializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.name', read_only=True)
    key_players = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(role='player')
    )
    class Meta:
        model=Team_Scouting_model
        fields=[
            'user',
            'report_title',
            'overview',
            'strengths',
            'weaknesses',
            'key_players',
            'tendencies',
            
            ]