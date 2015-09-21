#!/usr/bin/env python
import facebook

def post_on_fb(oauth_token, post_title, link, description):
    """
    Method takes authentitation token, post title, link and description and 
    makes a post on Facebook.
    """
    post = {
      'name': post_title,
      'link': link,
      'description': description
    }

    facebook_graph = facebook.GraphAPI(oauth_token)
    try:
        response = facebook_graph.put_wall_post('', attachment=post)
    except facebook.GraphAPIError as e:
        print e
        
        