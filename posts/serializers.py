from rest_framework import serializers
from rest_framework.exceptions import NotFound

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


class ReverseCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection

        fields = (
            'id',
            'name',
            'body_text',
            'bg_img_url',
            'updated',
            'created'
        )
        read_only_fields = ('id', 'updated', 'created')


class PostCollectorSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, required=False)
    collection_set = ReverseCollectionSerializer(read_only=True, many=True)

    class Meta:
        model = Post

        fields = (
            'id',
            'owner',
            'title',
            'body_text',
            'bg_img_url',
            'collection_set',
            'updated',
            'created'
        )
        read_only_fields = ('id', 'owner', 'title', 'body_text', 'bg_img_url', 'updated', 'created')

    def update(self, *args, **kwargs):
        try:
            collection = Collection.objects.get(pk=self.initial_data['collection_id'])
            post = self.instance
            post.collection_set.add(collection)
            post.save()
            return post
        except:
            raise NotFound('Colletion object not found')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostCollectorSerializer, self).get_validation_exclusions()

        return exclusions + ['owner']


class PostUnCollectorSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True, required=False)
    collection_set = ReverseCollectionSerializer(read_only=True, many=True)

    class Meta:
        model = Post

        fields = (
            'id',
            'owner',
            'title',
            'body_text',
            'bg_img_url',
            'collection_set',
            'updated',
            'created'
        )
        read_only_fields = ('id', 'owner', 'title', 'body_text', 'bg_img_url', 'updated', 'created')

    def update(self, *args, **kwargs):
        try:
            collection = Collection.objects.get(pk=self.initial_data['collection_id'])
            post = self.instance
            post.collection_set.remove(collection)
            post.save()
            return post
        except:
            raise NotFound('Colletion object not found')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostUnCollectorSerializer, self).get_validation_exclusions()

        return exclusions + ['owner']
