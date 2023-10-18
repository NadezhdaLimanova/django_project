from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter(field_name = "created_at")

    # def status_filter(self, data):
    #     user_adv = self.context["request"].user
    #     adv = Advertisement.objects.filter(creator=user_adv, status='OPEN').count()
    #
    #     return data

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at' ]





