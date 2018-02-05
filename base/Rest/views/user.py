# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from base.Rest.filters import UserFilter
from base.Rest.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from base.models import CustomUser


class UserListView(ReadOnlyModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = UserFilter
    permission_classes = (IsAuthenticated, )
    queryset = CustomUser.objects.all()
    ordering_fields = '__all__'


class RegisterView(CreateAPIView):
    model = CustomUser
    serializer_class = RegisterSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = UserFilter
    permission_classes = (AllowAny, )
    queryset = CustomUser.objects.all()
    ordering_fields = '__all__'


class LoginView(CreateAPIView):
    """
    for now permission classes will stay commented
    """
    model = CustomUser
    serializer_class = LoginSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = UserFilter
    permission_classes = (AllowAny, )
    queryset = CustomUser.objects.all()
    ordering_fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        pass
        password = serializer.validated_data['password']

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'Email does not exist!'})

        auth_user = authenticate(username=user.username, password=password)
        if auth_user is not None:
            Token.objects.get_or_create(user=auth_user)
            login(self.request, user)
            return Response({'message': 'Logged in Succesfully! Rediercting to the home page'})
            # A backend authenticated the credentials
        else:
            return Response({'message': 'Authentication failure. Check email and/or password!'})
            # No backend authenticated the credentials


class LogoutView(CreateAPIView):
    model = CustomUser
    serializer_class = LoginSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_class = UserFilter
    permission_classes = (IsAuthenticated, )
    queryset = CustomUser.objects.all()
    ordering_fields = '__all__'

    def perform_create(self, serializer):

        email = serializer.data['email']

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'Redirecting to register page. Please register to log in.'})

        logout(self.request)
        return Response({'message': 'Successfully Logged out!'})
