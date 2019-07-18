"""
O que este script de início rápido pretende fazer?
- atividade básica de seguir / deixar de seguir.
NOTAS:
- Não automatizar comentários e gostos
isso apenas para postar que realmente gostasse do conteúdo assim no momento só
use a função follow / unfollow.
- Eu uso dois arquivos "quickstart", um para seguir e outro para unfollow.
- notei que o mais importante é que a conta de onde eu
obter seguidores tem conteúdo semelhante ao meu, a fim de ter certeza de que o meu
conteúdo pode ser apreciado. Após o próximo passo, começo a deixar de seguir
o usuário que não me seguiu de volta.
"""

# imports
from instapy import InstaPy
from instapy import smart_run
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint


# login credentials
insta_username = 'Rodolfodsantos2019'
insta_password = '1e12e1e1'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=590,
                                    min_followers=45,
                                    min_following=77)

    #session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["vida", "#filosofia"])

    
    #LOCALIZAÇÃO EM TESTE
    #session.like_by_locations(['1064589636918209/gravata-recife/'], amount=100)
    # or
    #session.like_by_locations(['1064589636918209'], amount=100)
    # or include media entities from top posts section
    #session.like_by_locations(['1064589636918209'], amount=5, skip_top_posts=False)
    
    #Comment by Locations#
    #session.comment_by_locations(['1064589636918209/gravata-recife/'], amount=5)
    # or
    #session.comment_by_locations(['1064589636918209'], amount=5)
    # or include media entities from top posts section
    #session.comment_by_locations(['1064589636918209'], amount=5, skip_top_posts=False)
    
    #Follow by Locations
    #session.follow_by_locations(['1064589636918209/gravata-recife/'], amount=5)
    # or
    #session.follow_by_locations(['1064589636918209'], amount=5)
    # or include media entities from top posts section
    #session.follow_by_locations(['1064589636918209'], amount=5, skip_top_posts=False)


    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """
    session.follow_user_followers(['marcelo_de_brito'], amount=3500,
                                  randomize=False, interact=True)

    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=3500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)
    #Atrasos
    #session.set_action_delays(enabled=True, like=5.2, randomize=True, random_range=(70, 140))

    """ Second step of Massive Follow...
    """
    session.follow_user_followers(['marcelo_de_brito'], amount=3500,
    #                             randomize=True, interact=True)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=3500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)


    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice shot! @{}',
        'Awesome! @{}',
        'Cool :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Nice @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods()
