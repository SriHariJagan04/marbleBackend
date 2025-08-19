from rest_framework import serializers

class EnquirySerializer(serializers.Serializer):
    product = serializers.CharField(max_length=255)
    description = serializers.CharField()
    name = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=20)
    email = serializers.EmailField()
