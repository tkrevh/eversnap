from rest_framework import serializers
from models import Picture, TUser, Album

# Definitions required by REST API framework
class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'url', 'likes', 'image', 'user', 'album', 'date_created')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'name', 'max_id')

class TUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TUser
        fields = ('id', 'name', 'screen_name')

