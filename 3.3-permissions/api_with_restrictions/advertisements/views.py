from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement

from advertisements.serializers import AdvertisementSerializer

from advertisements.permissions import IsOwnerOrReadOnly

from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filterset_class = AdvertisementFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
