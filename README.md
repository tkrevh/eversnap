# eversnap 
===========
TweetsAlbum
===========

TweetsAlbum enables users to download specific images from Twitter
and then creates an album for every different hashtag. Typical usage
often looks like this::

    ./python twitter.py #carnival 20

Purpose of this code
====================

This code was written as an assignment for a Job interview at Eversnap (www.geteversnap.com).
We had 2 days to deliver the solution. These were the instructions:

Welcome to the Django Assignment

The goal of the homework is to build a fully functional django app using standard best practices and reusable code.


Part A)

The app that we are going to build is going to be a smart automatic album creator. The app should create an album, run every 20min and fetch the last photos posted on twitter (under the hashtag #carnival) since the last fetching. Every picture need to be stored in the album model and associated with its user.

When the album reach 100 photos send an email to yourself & CC davide@geteversnap.com 
From: Eversnap Hashtag
From Email: Hashtag@EversnapApp.com
To: Your email address
Bcc: davide@geteversnap.com 
Subject: #carnival has 100 photos [100 should change to 200, when the album reaches that many photos and so on.] 
Body: I’m awesome! 

PS. There shouldn’t be any duplicate photos (Hint: Try to avoid Photos with duplicate URLs)

The emails should stop after the album reaches 501 photos. 

At any point in time you should be able to see the photos that are stored in your album in 2 different ways.
1) Accessing a url in your browser that shows all the pictures
2) Accessing a REST api that shows you the data structure of the pictures in your album

When the app is complete a customer is asking you to improve the model and add also a DateTime field to store the moment when the picture has been stored in your album.

Automated Tests are required for point 1) and 2)


Part B)

Let’s assume that for each picture it is stored also the number of likes and his owner.
There should be a function that creates a collage of the most 7 popular photos in the album and export it to facebook with the link to the album.



Bonus points
Additional points are provided if the app is packaged (but not published) for pypi.
Estimated time
This assignment is planned to be completed in approximately 10-12 hours. Send the completed assignment to Mikaela@geteversnap.com exactly 2 days after you receive the email (at the latest), and she will forward the completed assignment to Davide.
Grading Criteria
In the order of importance:
1) Functionality: The app functions as it is described in the assignment (7 points)
2) Quality of Code: The code follows general conventions and python standards (5 points)
3) Clearness: Keep it simple and clear to understand (3 points)
4) Time to solve (2 points)


Frequently Asked Questions
Q: If I take more time to solve, can I deliver the code anyway?
A: Yes, but there's points related to the time that you’re going to lose.
Q: What if I have other questions?
A: You can ask davide@geteversnap.com or you can just make assumptions but make sure to say what assumptions you have made. 




