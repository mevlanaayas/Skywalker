# -*- coding: utf-8 -*-
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from base.Rest.filters import PointBasedMapFilter
from base.Rest.serializers import PointBasedMapSerializer
from base.functions.gzip import gzip_op
from base.functions.visualization import save_map, save_movement, save_label
from base.models import PointBasedMap, Map


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

    def synchronize(self, *args):
        """
        current_maps = PointBasedMap.objects.values('id')
        remaining_maps = Map.objects.filter(pk__in=current_maps)
        """
        current_maps = PointBasedMap.objects.all()
        all_maps = Map.objects.all()
        remaining_maps = set(all_maps).difference(set(current_maps))
        for map_instance in remaining_maps:
            temp_map = PointBasedMap()
            extracted_map_data = gzip_op(map_instance.map_data)
            extracted_initial_data = gzip_op(map_instance.initial_data)
            extracted_movement_data = gzip_op(map_instance.movement_data)
            extracted_label_data = gzip_op(map_instance.label_data)
            advanced_initial_data = save_map(extracted_initial_data)
            advanced_point_data = save_map(extracted_map_data)
            advanced_movement_data = save_movement(extracted_movement_data)
            advanced_label_data = save_label(extracted_label_data)
            temp_map.advanced_points = None
            temp_map.label_data =None
            temp_map.initial_points = None
            temp_map.movement_points = None
        """
        label_data = validated_data['label_data']
        extracted_label_data = gzip_op(label_data)
        advanced_initial_data = save_map(extracted_map_data)
        advanced_point_data = save_map(str(new_map_data))
        advanced_movement_data = save_movement(extracted_movement_data)
        advanced_label_data = save_label(extracted_label_data)
        """
        a = 5
        return a
