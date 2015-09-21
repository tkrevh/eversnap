#!/usr/bin/env python
import os
import sys
import csv
import datetime
import logging
import tweepy
import threading
import getopt
 
from django.core.mail import EmailMessage

os.environ['DJANGO_SETTINGS_MODULE'] = 'Eversnap.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eversnap.settings")
from tweetsalbum.models import Album, TUser, Picture

SEND_EMAIL_EVERY_N_PICTURES = 100
SEND_EMAIL_UNTIL_MAX_PICTURES = 500


# Setup Logger
logger = logging.getLogger('tweets_album_import')
hdlr = logging.FileHandler('tweets_album_import.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

# Setup Twitter OAuth keys
CONSUMER_KEY = 'xFMnX9Gc5A4BwaS1J3lz4jKFi'
CONSUMER_SECRET = 'OcmfhbTMBZ0THzobK7N1G0wtqi50MN7KQUYTAWlBgi8Mpw4wBd'
ACCESS_TOKEN = '1483497169-GV7gnVoMfoJVAKwNwmgqXXQv7cdAh5jf4G33Zkq'
ACCESS_TOKEN_SECRET = '6OkPU1iKzjw2ww7oVXB9OC3ELEwPXE0qp92adEQkXWreg'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
# Create Twitter API interface
api = tweepy.API(auth)


def do_every(interval, worker_func, hashtag, iterations = 0):
    """
    Method schedules a function to execute at consecutive intervals for
    N interations. When N=0, it executes infinitely.
    """
    if iterations != 1:
        threading.Timer(
            interval, 
            do_every, 
            [interval, worker_func, hashtag, 0 if iterations == 0 else iterations-1]
        ).start();
        
    worker_func(hashtag)
        
def must_send_email(picture_count):
    """
    Send mail for every SEND_EMAIL_EVERY_N_PICTURES downloaded Pictures, but 
    not after more then SEND_EMAIL_UNTIL_MAX_PICTURES Pictures have been 
    downloaded.
    """
    return (picture_count <= SEND_EMAIL_UNTIL_MAX_PICTURES and picture_count % SEND_EMAIL_EVERY_N_PICTURES == 0)
    
def send_mail(hashtag, picture_count):
    """
    Sends email notification
    """
    subject = '%s has %d photos' % (hashtag, picture_count)
    body = "I'm awesome!"
    from_address = 'Eversnap Hashtag <Hashtag@EversnapApp.com>'
    to_address = ['tadej.krevh@gmail.com']
    bcc = ['davide@geteversnap.com']
    
    try:
        email = EmailMessage(subject, body, from_address, to_address, bcc)
        email.send()
        logger.info('Email sent: '+subject)
    except Exception, error:
        logger.warn('Unable to send email: %s' % (error));

def fetch_twitter_images(hashtag): 
    """
    Fetches Twitter images for given hashtag. It creates or loads an Album 
    with hashtag, then creates or loads Twitter User and then finally saves 
    the Picture if picture with same URL address does not yet exist.
    An Email notification is sent for every N downloaded pictures. 
    Also, the highest ID of the tweet is saved for next API search which then 
    searches from this ID onwards (for newer posts).
    """
    
    logger.info('Fetching Twitter images for %s' % (hashtag))
    album_name = hashtag.translate(None, '#')
    album, created = Album.objects.get_or_create(name=album_name)
    if created:
        album.save()
        logger.info('Album %s created' % (album_name))
    else:
        logger.info('Album %s loaded' % (album_name))
    logger.info('Fetching all tweets with ID > %d' % (album.max_id))
    for tweet in tweepy.Cursor(api.search,
                                        q=hashtag+' filter:images',
                                        count=100,
                                        result_type='recent',
                                        include_entities=True,
                                        since_id=album.max_id).items():
        if tweet.entities.has_key('media'):
            medias = tweet.entities['media']
            for m in medias :
                media_url = m['media_url']
                logger.info('Fetched tweet ID:%d posted by @%s -> %s' % (tweet.id, tweet.user.screen_name, media_url))
                
                # first check if user already exists, if not, create one
                user, created = TUser.objects.get_or_create(screen_name=tweet.user.screen_name)
                if created:
                    user.name = tweet.user.name
                    user.save()
                    logger.info('Twitter User %s created' % (user.screen_name))
                else:
                    logger.info('Twitter User %s loaded' % (user.screen_name))

                # if pictures does not yet exist, create it -> TODO: need to 
                # find a better way how to assure that images are not 
                # duplicated, because once uploaded to twitter, they get a 
                # unique name
                if not Picture.objects.filter(url = media_url).exists():
                    picture = Picture()
                    picture.url = media_url
                    picture.album = album
                    picture.user = user
                    picture.save()
                    logger.info('Picture %s created' % (picture.url))
                    # send email notification after every N pictures are fetched
                    picture_count = Picture.objects.filter(album=album).count()
                    if must_send_email(picture_count):
                        send_mail(hashtag, picture_count)
                else:
                    logger.info('Picture %s already exists' % (media_url))
                    
                # store max_id value for next round of fetching
                if tweet.id > album.max_id:
                    album.max_id = tweet.id
                    logger.info('Max ID: %d' % (tweet.id))
                    album.save()
          
def main():
    if len(sys.argv) < 2:
        print 'Parameters: <hashtag> <fetch_interval_in_minutes>\n'
        print 'Example: '+sys.argv[0]+' #carnival 20\n'
        sys.exit(-1)
    
    hashtag = sys.argv[1]
    interval_in_minutes = int(sys.argv[2])
    # run it once, then again every X minutes
    do_every (interval_in_minutes*60, fetch_twitter_images, hashtag);

if __name__ == "__main__":
     main()
     
     