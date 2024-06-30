from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    #   сериализаторов и фильтров
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

    def get_queryset_status(self):
        """Фильтрация queryset по статусу и дате`."""
        queryset = self.queryset
        return queryset.filter(status=self.request.user)

    def get_queryset_date(self):
        """Фильтрация queryset по дате."""
        queryset = self.queryset
        return queryset.filter(created_at__gte=self.request.user)

