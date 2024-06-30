from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры


    class Meta:
        model = Advertisement
        fields = ['id', 'status', 'created_at', 'updated_at']


