# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from base.Rest.views.label import LabelView
from base.Rest.views.map import MapView
from base.Rest.views.qr import KRView
from base.Rest.views.user import UserListView, RegisterView
from rest_auth.views import LoginView, LogoutView


router = DefaultRouter()
router.register(r'map', MapView)
router.register(r'label', LabelView)
router.register(r'user', UserListView)
router.register(r'qr', KRView)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(), name="login"),
]
