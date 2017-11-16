from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from model.models.userdata import UserData


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        try:
            email = request.data['email']
            password = request.data['password']
        except KeyError as e:
            return HttpResponse(str(e.args[0]) + 'is missing!', status=400)

        new_user = User()

        new_user.username = email
        new_user.set_password(password)
        new_user.save()

        UserData.objects.create(user=new_user)

        token = Token.objects.create(user=new_user)

        return HttpResponse(token)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        try:
            email = request.data['email']
            password = request.data['password']
        except KeyError as e:
            return HttpResponse(str(e.args[0]) + 'is missing!', status=400)

        user = authenticate(request, username=email, password=password)

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return JsonResponse({"sessionID": str(token)})

        return JsonResponse({"Error": "unauthorized"})


class LogoutView(APIView):
    queryset = User.objects.all()

    def get(self, request):
        request.user.auth_token.delete()
        return HttpResponse()
