from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BlogSerializer
from .models import Blog
from django.shortcuts import get_object_or_404

class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            blogs = Blog.objects.filter(user=request.user)

            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(title__icontains=search) | blogs.filter(blog_text__icontains=search)

            serializer = BlogSerializer(blogs, many=True)
            return Response({
                'data': serializer.data,
                'message': 'Content fetched successfully'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)  # Log the exception for debugging
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()
                response_data = serializer.data
                response_data['message'] = 'Content created successfully'
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation error: Please check input data'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)  # Log the exception for debugging
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, content_id):
        try:
            blog = get_object_or_404(Blog, content_id=content_id)

            if blog.user != request.user:
                return Response({
                    'message': 'You do not have permission to update this blog post'
                }, status=status.HTTP_403_FORBIDDEN)

            serializer = BlogSerializer(blog, data=request.data, partial=True, context={'request': request})

            if serializer.is_valid():
                serializer.save()
                response_data = serializer.data
                response_data['message'] = 'Content updated successfully'
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation error: Please check input data'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)  # Log the exception for debugging
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
