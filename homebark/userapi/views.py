from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,Quote
from .serializers import Inputdata,Outputdata,UserRegistration
from .service import outputservice
from django.db import IntegrityError
from rest_framework import permissions, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect 
from django.views.decorators.http import require_POST

class UserView(APIView):
    permission_classes=[]
    authorization_classes=[]

    def post(self,request):
        serialiser = UserRegistration(data=request.data)
        try:
            if serialiser.is_valid():
                username = serialiser.validated_data['username']
                password = serialiser.validated_data['password']
                User.objects.create_user(username=username, password=password)
                return Response({'message':'user created'},status=status.HTTP_200_OK)
        except:
            return Response({'serializererror':'try again'},status=status.HTTP_400_BAD_REQUEST)

class QuotesView(APIView):
    permission_classes=[IsAuthenticated]
    authorization_classes=[JWTAuthentication]
    def get(self,request):
        serializer = Inputdata(data=request.query_params)
        if serializer.is_valid():
            result = outputservice(
                count = serializer.validated_data['count']
            )

            output = Outputdata(result,many=True)

            return Response(output.data)
        else:
            return Response({'serializer_error':'invalid'},status=status.HTTP_400_BAD_REQUEST)

def custom_logout_view(request):
        logout(request)
        