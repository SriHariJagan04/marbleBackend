from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer, TestimonialSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Testimonials

# Create your views here.

# Anyone can list/create testimonials
class TestimonialCreateListView(generics.ListCreateAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny]

# Only admin can update/delete
class TestimonialUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
