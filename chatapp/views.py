from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .models import Users
from .serializer import *
import jwt
import datetime
import os
from dotenv import load_dotenv
from django.core.cache import cache

# Create your views here.

class Register(APIView):
    def post(self, request):
        data = request.data
        serializer= UsersSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Registered successfully"}, status=201)
        return Response({"message":"Something went wrong"}, status=500)
class Login(APIView):
    def post(self, request):
        data = request.data
        try:
            # user=None
            # if data["username"] not in cache:
            user =Users.objects.filter(username=data["username"]).first()
                # cache.set(data["username"], user, timeout=(60*30)) # 30 minutes
            # else:
                # user = cache.get(data["username"])
            if user:
                if(check_password( data["password"], user.password)):
                    load_dotenv()
                    SECRET_KEY=os.getenv('SECRET_KEY')
                    payload = {
                        "username":user.username,
                        "exp":int(datetime.datetime.now().timestamp())+(60*60), # 1 hour expiration
                        "iat":int(datetime.datetime.now().timestamp())
                    }
                    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                    return Response({"message":"login success","token":token},status=200)
            return Response({"message":"login failed"},status=400)
        except Exception as e:
            # print(e)
            return Response({"message":"Something went wrong"},status=500)
            

class CronJob(APIView):
    def get(self, request):
        return Response({"message":"Cron job executed"}, status=200)