Steps:
1. Installation of additional modules:
    a) pip install tweepy
    b) pip install mysql-python
    c) pip install South
    d) pip install djangorestframework
    e) pip install facebook-sdk

2. Create MySQL DB and environment
    a) Database Name: tweetsalbum
    b) Username: tweetsalbum
    c) Password: tweetsalbum..
    OR create another DB and edit settings.py accordingly
    Grant required rights to user (also to be able to create database for tests)
    d) Edit settings.py to reflect the different installation directory / environment    
    
3. Optional - run local mail server simulator for testing purposes (OR setup SMTP server that can send as Hashtag@EversnapApp.com)
    a) python -m smtpd -n -c DebuggingServer localhost:1025
    
4. Sync database
    a) manage.py syncdb
    b) python manage.py migrate
    
5. Run tests
    a) python manage.py test tweetsalbum
    
6. Fetch Twitter Data
    a) python twitter.py #carnival 20
    b) it is possible to change hashtag and sleep time (in minutes) -> for each hashtag a new album is created

7. Local setup
    a) Add "127.0.0.1       tweetsalbum.com" to hosts file because Facebook requires FQDN
    b) python manage.py runserver 
    
8. Facebook setup
    a) Created TweetsAlbum FB App
    b) Created Access Token via FB Graph API Explorer for TweetsAlbum
    c) Example usage (token may expire and you may need a new one):
    import fbpost
    fbpost.post_on_fb('CAAUe5HIdgAEBABIB1UOO4NSZAvexEx4pXjcsE1Cfwc1ZAsFkppqklAtVFSwKuksCMqCFtdNN0zYDBOqu5qZBwq80UUhjcIts7ngYWhOfaOyXzswoGzl9RZBDxFmPZCAygQDh5A9r3WeFyFf3lLauB3T4RvIPyMzS1ZAsZBJgutWVcW82vZCocZA8MYaR8cXZBnQxMZD', '7 most liked pictures at tweetsalbum.com', 'http://tweetsalbum.com:8000/favorites/carnival/', 'Twitter images tagged #carnival')
    
9. Available URLs:
    a) add tweetsalbum.com to hosts file to point to localhost, or use 127.0.0.1 or 'localhost' instead of tweetsalbum.com
    b) http://tweetsalbum.com:8000/pictures/                - displays all pictures
    c) http://tweetsalbum.com:8000/favorites/               - displays top 7 liked pictures from all albums (hint: change number of likes on picture in admin backend -> http://tweetsalbum.com:8000/admin/)
    d) http://tweetsalbum.com:8000/favorites/carnival/      - displays top 7 liked pictures in album carnival (change likes number manually as all pictures are initialized with 0 likes)
    e) http://tweetsalbum.com:8000/api/pictures/            - REST API for Pictures
    f) http://tweetsalbum.com:8000/api/tusers/              - REST API for Twitter Users
    g) http://tweetsalbum.com:8000/api/albums/              - REST API for Albums
        

KNOWN ISSUES:
- Sometimes duplicate images are downloaded, but this is due to images having different filenames. More complex algorithm is required to avoid duplicates.