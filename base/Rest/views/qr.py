# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.Rest.filters import KRFilter
from base.Rest.serializers import KRSerializer
from base.functions.kr import create_kr, combine_images, send_kr
from base.models import KR, Map


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
        del serializer.validated_data['del']
        self.perform_create(serializer)

        kr_id = serializer.data['id']
        create_kr(kr_id)
        combine_images()
        send_kr(email)

        return super(KRView, self).create(request, args, kwargs)

