from rest_framework import viewsets, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.serializers import UserSerializer
from api.permissions import IsAdminReadOnly, IsSuperadmin


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserToAdmin(views.APIView):
    permission_classes = [IsSuperadmin, ]

    def get(self, request, id):
        user = User.objects.get(pk=id)
        user.is_staff = True
        user.save()

        return Response()


class UserRemoveAdmin(views.APIView):
    permission_classes = [IsSuperadmin, ]

    def get(self, request, id):
        user = User.objects.get(pk=id)
        user.is_staff = False
        user.save()

        return Response()
