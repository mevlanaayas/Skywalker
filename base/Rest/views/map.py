# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'map_name': serializer.data['name'], 'op': 'created'}, headers=headers,
                        status=status.HTTP_201_CREATED)
