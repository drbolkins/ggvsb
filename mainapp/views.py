from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.parsers import JSONParser
import json


class testing(APIView):
    def get(self,request):
        content = {"test" : "testing done"}
        return Response(content)


class LoginView(APIView):

    parser_classes = (JSONParser,)

    def post(self, request, format=None):

        jsonResponse = json.loads(request.body.decode('utf-8'))
        usern = jsonResponse["username"]
        passw = jsonResponse["password"]
        user = authenticate(request, username=usern,password=passw)

        if user is not None:
            content = {"user": user.username, "email": user.email}
            login(request, user)
            return Response(content)
        content = {"nope": jsonResponse}
        return Response(content)

class LogoutView(APIView):
    def get(self,request):
        logout(request)
        return Response({"logged_out": True})

