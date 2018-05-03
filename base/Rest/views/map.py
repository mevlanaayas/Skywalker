# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from base.Rest.filters import MapFilter
from base.Rest.serializers import MapSerializer
from base.models import Map, KR


class MapView(ModelViewSet):
    model = Map
    serializer_class = MapSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = MapFilter
    permission_classes = (AllowAny, )
    queryset = Map.objects.all()
    lookup_field = 'qr_id'
    ordering_fields = ('created_at', 'updated_at')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        qr_id = serializer.validated_data['qr_id']
        self.perform_create(serializer)
        map_id = serializer.data['id']
        updated_kr = KR.objects.get(id=qr_id)
        updated_kr.map_id = map_id
        updated_kr.save()
        headers = self.get_success_headers(serializer.data)
        return Response({'map_name': serializer.data['name'], 'op': 'created'}, headers=headers,
                        status=status.HTTP_201_CREATED)
