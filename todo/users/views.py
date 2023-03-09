from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
