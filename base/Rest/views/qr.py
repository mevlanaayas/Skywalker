# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.Rest.filters import KRFilter
from base.Rest.serializers import KRSerializer
from base.models import KR


class KRView(ModelViewSet):
    model = KR
    serializer_class = KRSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = KRFilter
    permission_classes = (AllowAny, )
    queryset = KR.objects.all()
    ordering_fields = '__all__'
