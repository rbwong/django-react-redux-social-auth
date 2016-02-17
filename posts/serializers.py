from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post, Collection


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = (
            'id',
            'owner',
            'title',
            'body_text',
            'bg_img_url',
            'updated',
            'created'
        )
        read_only_fields = ('id', 'updated', 'created')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['owner']


class CollectionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, required=False)
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Collection

        fields = (
            'id',
            'owner',
            'name',
            'body_text',
            'bg_img_url',
            'posts',
            'updated',
            'created'
        )
        read_only_fields = ('id', 'updated', 'created')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(CollectionSerializer, self).get_validation_exclusions()

        return exclusions + ['owner']
