from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            user_token = token = AuthToken.objects.create(user)
            response = {"token": user_token}
            return Response(response, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class ExampleView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'foo': 'bar'
        }
        return Response(content)






