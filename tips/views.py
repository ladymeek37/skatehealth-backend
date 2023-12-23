# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Tip
from .serializers import TipSerializer
from favorite_tips.models import FavoriteTip
# Create your views here.

#api request to get all tips
@api_view(['GET'])
@permission_classes([AllowAny])
def tips_list(request):
    tips = Tip.objects.all()
    serializer = TipSerializer(tips, many=True)
    return Response(serializer.data)


#api request to post a new tip/request to get tips by user ID
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_tip(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = TipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        tips = Tip.objects.filter(user_id=request.user.id)
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)

#api request to update and delete tip
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tip_detail(request, pk):
    tip = get_object_or_404(Tip, pk = pk)
    if request.method == 'PUT':
        serializer = TipSerializer(tip, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        tip.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#api request to get tips by category
@api_view(['GET'])
@permission_classes([AllowAny])
def tips_by_category(request):
    category_param = request.query_params.get('category')
    tips = Tip.objects.all()

    if category_param:
        tips = tips.filter(category = category_param)

    serializer = TipSerializer(tips, many=True)
    return Response(serializer.data)


#api request to get tip by id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_tip_by_id(request, tip_id):
    tip = Tip.objects.filter(id = tip_id)
    serializer = TipSerializer(tip, many=True)
    return Response(serializer.data)


#request to add to favorite count
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def add_to_fav_count(request, pk):
    tip = get_object_or_404(Tip, pk = pk)
    check_tip = FavoriteTip.objects.filter(user=request.user,tip_id = pk).exists()
    if check_tip == True:
        return Response("Already favorited!")
    tip.favorite_count = tip.favorite_count + 1
    serializer = TipSerializer(tip, data = request.data, partial = True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)



