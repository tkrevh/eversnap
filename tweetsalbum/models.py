import datetime
import urllib2

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import timedelta, date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
from PIL import Image
from StringIO import StringIO
from urlparse import urlparse
from os.path import splitext, basename

class Album(models.Model):
    """
    Model of Album. Holds albums name and max_id, which is used for subsequent 
    queries.
    """
    name = models.CharField(max_length=64)
    max_id = models.BigIntegerField(default=0)
    
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums") 

    def __unicode__(self):
        return u'Album #%s' % (self.name)        

class TUser(models.Model):
    """
    Model of Twitter User. We store name and screen_name.
    """
    name = models.CharField(max_length=64)
    screen_name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = _("Tweeter User")
        verbose_name_plural = _("Tweeter Users") 

    def __unicode__(self):
        return u'User @%s' % (self.screen_name)        

class Picture(models.Model):
    """
    Model of pictures. Has foreign keys on Album and TUser, but also url to 
    downloaded image, link to locally stored image, number of likes and 
    timestamp of creation.
    """
    album = models.ForeignKey(Album)
    user = models.ForeignKey(TUser)
    likes = models.IntegerField(default=0)
    image = models.ImageField(_("Image"), upload_to="downloaded_images/", blank=False, null=False)
    # unique=True is not supported for character fields in size over 255 chars
    # in mysql, so we'll check for URL uniqueness before creating new instance
    url = models.CharField(max_length=2000, blank=False, null=False)
    date_created = models.DateTimeField(_("Date created"), default=datetime.datetime.now)
    
    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures") 
        ordering = ('-likes',)

    def __unicode__(self):
        return u'(%s) @%s %s [%s]' % (self.album.name, self.user.screen_name, self.url, self.likes)        

    def download_image(self, url):
        """
        Downloads an image and stores it as a JPEG locally. File name is preserved.
        """
        input_file = StringIO(urllib2.urlopen(url).read())
        output_file = StringIO()
        img = Image.open(input_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(output_file, "JPEG")
        disassembled = urlparse(url)
        filename, file_ext = splitext(basename(disassembled.path))
        self.image.save(filename+".jpg", ContentFile(output_file.getvalue()), save=False)

    def save(self, *args, **kwargs):
        """
        Make sure we download the image if not yet downloaded, when we save the object.
        """
        if not self.image:
            self.download_image(self.url)
        super(Picture, self).save(*args, **kwargs)      
        