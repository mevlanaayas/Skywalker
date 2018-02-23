from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.Rest.filters import LabelFilter
from base.Rest.serializers import LabelSerializer
from base.models import Label


class LabelView(ModelViewSet):
    model = Label
    serializer_class = LabelSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = LabelFilter
    permission_classes = (AllowAny, )
    queryset = Label.objects.all()
    ordering_fields = '__all__'
