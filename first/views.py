from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSignupSerializer

from django.contrib.auth import logout

# Create your views here.

class UserSignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    
    # def __init__(self, extra=None, **kwargs):
    #     self.extra = extra
    #     super(UserSignupViewSet, self).__init__(**kwargs)
        
    # @classmethod
    # def as_view(cls, extra=None,*args, **kwargs):
    #     view = super(UserSignupViewSet, cls).as_view(*args, **kwargs)
    #     view.extra = extra
        
    #     return view
        

class UserViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    
def logout_user(request):
    logout(request)
    
    return redirect(to="register-user")