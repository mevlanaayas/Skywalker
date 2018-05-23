# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from base.Rest.filters import PointBasedMapFilter
from base.Rest.serializers import PointBasedMapSerializer
from base.models import PointBasedMap


class VueView(ModelViewSet):
    model = PointBasedMap
    serializer_class = PointBasedMapSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = PointBasedMapFilter
    permission_classes = (IsAuthenticated, )
    queryset = PointBasedMap.objects.all()
    ordering_fields = ('created_at', 'updated_at')

    def get_queryset(self):
        queryset = PointBasedMap.objects.filter(created_by=self.request.user.email)
        return queryset
