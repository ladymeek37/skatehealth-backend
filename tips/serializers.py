from rest_framework import serializers
from .models import Tip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['id', 'title', 'text', 'link', 'image_url', 'favorite_count', 'date', 'category', 'user', 'category_display']
        depth = 2
    category_display = serializers.CharField(source='get_category_display', required = False)    