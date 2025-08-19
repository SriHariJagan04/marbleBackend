from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Testimonials


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
from rest_framework import serializers
from .models import Testimonials

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = [
            "id",
            "name",
            "company",
            "review",
            "rating",
            "linkedin",
            "website",
            "twitter",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

