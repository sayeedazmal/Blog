from rest_framework import serializers
from web_blog.models import Category


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","slug","created_date","update_date"]

# class TodoSerializer(serializers.Serializer):
    
    # name            = serializers.CharField(max_length=50)
    # banner_img      = serializers.ImageField()
    # slug            = serializers.SlugField()
    # created_date    = serializers.DateTimeField()
    # update_date     = serializers.DateTimeField()