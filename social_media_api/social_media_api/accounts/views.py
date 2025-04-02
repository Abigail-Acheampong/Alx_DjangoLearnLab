from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserSerializer, TokenSerializer
from rest_framework.authentication import TokenAuthentication

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            token_serializer = TokenSerializer(token)
            return Response(token_serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = CustomUser.objects.get(username=request.data.get('username'))
        if user.check_password(request.data.get('password')):
            token, created = Token.objects.get_or_create(user=user)
            token_serializer = TokenSerializer(token)
            return Response(token_serializer.data)
        return Response({'detail': 'Invalid credentials'}, status=400)

class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
