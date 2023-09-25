from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    published = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at']