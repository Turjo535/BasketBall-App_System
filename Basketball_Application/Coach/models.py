from django.db import models
from UserAccount.models import User
# Create your models here.
class Team_Information_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opponent_team_name=models.CharField(max_length=200)
    jersey_color=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    circuit_or_level=models.CharField(200)
    game_date=models.DateTimeField()
    performance_note=models.TextField()
    youtube_link=models.URLField()
    uploaded_video=models.FileField(upload_to="video/%y",blank=True, null=True)

class Team_Scouting_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_title = models.CharField(max_length=200)
    overview = models.TextField()
    strengths = models.JSONField()  
    weaknesses = models.JSONField()  
    key_players = models.ManyToManyField(
        User,
        related_name='key_players',
        limit_choices_to={'role': 'player'},
        
          
    )
    tendencies = models.TextField()

