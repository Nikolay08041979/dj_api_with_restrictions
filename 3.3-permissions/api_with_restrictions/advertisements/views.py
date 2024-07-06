from django.db.migrations import serializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissoins import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    #   сериализаторов и фильтров
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "update" or self.action == "partial_update":
            return [permissions.BasePermission]

    def get_queryset_status(self):
        """Фильтрация queryset по статусу и дате`."""
        queryset = self.queryset
        AdvertisementFilter.Meta.fields = ['status', 'created_at']
        return queryset

    def get_queryset_date(self):
        """Фильтрация queryset по дате."""
        queryset = self.queryset
        AdvertisementFilter.Meta.fields = ['created_at', 'updated_at']
        return queryset

