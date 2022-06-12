from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from .permissions import IsOwner
from clothes import models


class ClothesViewset(viewsets.ModelViewSet):
    queryset = models.Clothes.objects.all()
    serializer_class = serializers.ClothesSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]
