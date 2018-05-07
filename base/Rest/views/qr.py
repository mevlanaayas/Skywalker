# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from base.Rest.filters import KRFilter
from base.Rest.serializers import KRSerializer
from base.functions.kr import create_kr, send_kr
from base.models import KR
from rest_framework.response import Response


class KRView(ModelViewSet):
    model = KR
    serializer_class = KRSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = KRFilter
    permission_classes = (AllowAny, )
    queryset = KR.objects.all()
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        self.perform_create(serializer)
        kr_id = serializer.data['id']
        created_kr = KR.objects.get(id=kr_id)
        created_kr.created_by = email
        created_kr.save()
        create_kr(kr_id)
        send_kr(email, kr_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
