from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для комментариев.
    """
    author_id = serializers.ReadOnlyField(source="author.pk")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    ad_id = serializers.ReadOnlyField(source="ad.pk")

    class Meta:
        model = Comment
        exclude = ['author', 'ad']  # fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка объявлений.
    """
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для одного объявления.
    """
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    class Meta:
        model = Ad
        fields = '__all__'
