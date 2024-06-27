# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BlogSerializer
from .models import Blog
from django.shortcuts import get_object_or_404
from django.db.models import Count
import random

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
            print(e)
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()  # Remove passing user=request.user here
                response_data = serializer.data
                response_data['message'] = 'Content created successfully'
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation error: Please check input data'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, content_id):
        try:
            blog = get_object_or_404(Blog, id=content_id)

            if blog.user != request.user:
                return Response({
                    'message': 'You do not have permission to update this blog post'
                }, status=status.HTTP_403_FORBIDDEN)

            serializer = BlogSerializer(blog, data=request.data, partial=True, context={'request': request})

            if serializer.is_valid():
                serializer.save(user=request.user)  # Pass 'user' to serializer context
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
        

    def delete(self, request, content_id):
        try:
            blog = get_object_or_404(Blog, id=content_id)

            if blog.user != request.user:
                return Response({
                    'message': 'You do not have permission to delete this blog post'
                }, status=status.HTTP_403_FORBIDDEN)

            blog.delete()

            return Response({
                'message': 'Content deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            print(e)  # Log the exception for debugging
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def get_random_blog(self):
        try:
            # Count all blog posts
            count = Blog.objects.count()

            # Get a random index within the range of count
            random_index = random.randint(0, count - 1)

            # Fetch a single random blog post using offset and limit
            random_blog = Blog.objects.all()[random_index]

            return random_blog

        except Exception as e:
            print(e)  # Log the exception for debugging
            return None

    def get(self, request):
        try:
            if request.GET.get('random'):
                random_blog = self.get_random_blog()

                if random_blog:
                    serializer = BlogSerializer(random_blog)
                    return Response({
                        'data': serializer.data,
                        'message': 'Random blog fetched successfully'
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        'data': {},
                        'message': 'No blog posts available'
                    }, status=status.HTTP_404_NOT_FOUND)

            else:
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
            print(e)
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
