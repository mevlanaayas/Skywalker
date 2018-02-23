# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.Rest.filters import MapFilter
from base.Rest.serializers import MapSerializer
from base.models import Map


class MapView(ModelViewSet):
    model = Map
    serializer_class = MapSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = MapFilter
    permission_classes = (AllowAny, )
    queryset = Map.objects.all()
    ordering_fields = '__all__'
