import django_filters
from ads.models import Ad, Comment


class AdFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтр для объявлений по полям: название, описание, автор.
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )
    description = django_filters.CharFilter(field_name="description", lookup_expr="icontains", )
    author = django_filters.CharFilter(field_name="author", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title", "description", "author", )


class CommentFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтр для комментариев по полям: текст и автор.
    """
    author = django_filters.CharFilter(field_name="author", lookup_expr="icontains", )
    text = django_filters.CharFilter(field_name="text", lookup_expr="icontains")

    class Meta:
        model = Comment
        fields = ("author", "text", )
