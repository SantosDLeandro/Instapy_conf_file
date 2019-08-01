""" Quickstart script for InstaPy usage """

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'rodolfonatureza_2019'
insta_password = '1e12e1e1'

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

with smart_run(session):
    """ Activity flow """
    settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=4590,
                                        min_followers=45,
                                        min_following=77)
    
    #session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["pizza", "#store"])
    
    
    # actions
    session.set_do_comment(enabled=True, percentage=100)
    session.set_comments(['Gostei muito', 'Muito Bom', 'Vamos la'])
    session.like_by_tags(["terrenogravatá"])
