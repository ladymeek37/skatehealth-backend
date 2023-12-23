from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

# Create your views here.

#get all comments
@api_view(['GET'])
@permission_classes([AllowAny])
def comments_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    


#get comments by tip ID
@api_view(['GET'])
@permission_classes([AllowAny])
def comments_by_tip_id(request, tip_id):
    comments = Comment.objects.filter(tip_id=tip_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


#post new comment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#delete comment
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

