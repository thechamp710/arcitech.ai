from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    'data': {},
                    'message': 'Your account has been created successfully'
                }, status=status.HTTP_201_CREATED)
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

class LoginView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                response = serializer.get_jwt_token(serializer.validated_data)
                return Response(response, status=status.HTTP_200_OK)
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
