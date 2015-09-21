from django.shortcuts import render_to_response
from models import Picture, TUser, Album
from rest_framework import viewsets
from tweetsalbum.serializers import PictureSerializer, AlbumSerializer, TUserSerializer
from django.template import RequestContext

class TUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows twitter users to be viewed or edited.
    """
    queryset = TUser.objects.all()
    serializer_class = TUserSerializer


class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pictures to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    
    
class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer    
    

def favorites(request):
    """
    This view function returns the top 7 most liked Pictures from all Albums
    """
    most_liked_pictures = Picture.objects.all().order_by('-likes')[:7]
    return render_to_response('tweetsalbum/favorites.html', {'picture_list': most_liked_pictures}, context_instance=RequestContext(request))
    
def favorites_by_album(request, album):
    """
    This view function returns the top 7 most liked Pictures 
    from specified Album.
    """
    most_liked_pictures = Picture.objects.filter(album__name=album).order_by('-likes')[:7]
    return render_to_response('tweetsalbum/favorites.html', {'picture_list': most_liked_pictures, 'album': album}, context_instance=RequestContext(request))