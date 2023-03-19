from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter, CommentFilter


class AdPagination(pagination.PageNumberPagination):
    """
    Класс пагинации.
    """
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    """
    ViewSet для объявлений.
    """
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
        return super().get_permissions()

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для комментариев.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)


class AdModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet для фильтра по объявлениям.
    """
    filter_backends = (DjangoFilterBackend, )
    filterset_class = AdFilter


class CommentModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet для фильтра по комментариям.
    """
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CommentFilter
