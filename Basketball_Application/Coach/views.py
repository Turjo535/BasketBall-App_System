from django.shortcuts import render
from django.http import HttpResponse
from .serializers import Team_Information_Serializer,Team_Scouting_Serializer
from .models import Team_Information_model, Team_Scouting_model
from Players.permission import Is_Coach,IsOwner
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
class Team_Information_View(APIView):
    
    permission_classes=[Is_Coach,IsOwner, IsAuthenticated]
    def post(self, request):
        serializer = Team_Information_Serializer(data=request.data)
        #print(serializer)
        #print(request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Team information saved successfully.", status=201)
        else:
            return Response(serializer.errors, status=400)
        
class Team_Information_List_View(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        team=Team_Information_model.objects.all()
        serializer=Team_Information_Serializer(team, many=True)
        return Response(serializer.data, status=200)
        
class Team_Scouting_View(APIView):
    
    permission_classes=[Is_Coach,IsOwner, IsAuthenticated]
    def post(self, request):
        serializer = Team_Scouting_Serializer(data=request.data)
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("Team Scouting Information saved successfully.", status=201)
        else:
            return Response(serializer.errors, status=400)
        

class Team_Scouting_List_View(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        team=Team_Scouting_model.objects.all()
        serializer=Team_Scouting_Serializer(team, many=True)
        return Response(serializer.data, status=200)