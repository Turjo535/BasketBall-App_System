# permissions.py
from rest_framework import permissions
from UserAccount.models import User
class Is_Player(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if user is authenticated and has a Player profile
        #print(request.user.is_authenticated and hasattr(request.user, 'Player'),"This is Player")
        return request.user.is_authenticated and request.user.role=='player'
class Is_Coach(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role=='coach'

class IsOwner(permissions.BasePermission):
    
    
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated)