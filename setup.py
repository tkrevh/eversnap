from distutils.core import setup

setup(
    name='TweetsAlbum',
    version='0.1.0',
    author='Tadej Krevh',
    author_email='tadej.krevh@gmail.com',
    packages=['tweetsalbum'],
    scripts=['twitter.py','fbpost.py'],
    url='http://pypi.python.org/pypi/TweetsAlbum/',
    license='LICENSE.txt',
    description='Download hashtagged images from Twitter',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4.1",
        "facebook-sdk == 0.4.0",
        "tweepy == 2.3.0",
        "mysql-python == 1.2.5",
        "South >= 0.7.6",
        "djangorestframework == 2.3.14",
    ],
)