from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import FavoriteTip
from .serializers import FavoriteTipSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

#request to view favorited tips by user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_favorited_tips(request):
    favorite_tips = FavoriteTip.objects.filter(user_id=request.user.id)
    serializer = FavoriteTipSerializer(favorite_tips, many=True)
    return Response(serializer.data)


#request to add a tip to favorites
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request):
    #checks if tip has already been favorited by that user
    check_tip = FavoriteTip.objects.filter(user=request.user,tip_id = request.data["tip_id"]).exists()
    if check_tip == True:
        return Response("Already favorited!")
    elif check_tip == False:
        serializer = FavoriteTipSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

