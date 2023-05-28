from django.contrib.auth import get_user_model
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from panorbit_app.serializers import SignUpSerializer


class SignUp(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'gender': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'phone_number': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
            required=['first_name', 'last_name', 'gender', 'email', 'phone_number'],
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
        },
        operation_summary='Signup api',
        operation_description='api to create user',
        tags=['Custom Tag'],
    )
    def post(self, request) -> Response:
        serializer = SignUpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'signup.html')