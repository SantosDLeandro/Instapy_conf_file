"""
O que este script de início rápido pretende fazer?
- atividade básica de seguir / deixar de seguir.
NOTAS:
- Não automatiza comentários e gostos,
No momento só usa a função follow / unfollow.
- Nota é que a conta de onde eu vou
obter seguidores ter conteúdo semelhante ao meu, a fim de ter certeza de que o meu
conteúdo pode ser apreciado. Após o próximo passo, começo a deixar de seguir
o usuário que não me seguiu de volta dentro de 24h.
"""

# importações
from instapy import InstaPy
from instapy import smart_run
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import schedule
import time


# credenciais de login
insta_username = 'Rodolfodsantos2019'
insta_password = '1e12e1e1'

#Supervisor de cotas
"""Assuma o controle total das ações com as estratégias mais sofisticadas"""

session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(57, 585),
                               peak_comments=(21, 182),
                                peak_follows=(48, None),
                                 peak_unfollows=(35, 402),
                                  peak_server_calls=(None, 4700))


# obtenha uma sessão InstaPy!
# set headless_browser = True para executar o InstaPy em segundo plano
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)
                  
with smart_run(session, threaded=True):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers = 3000 ,
                                    max_following = 2000 ,
                                    min_followers = 100 ,
                                    min_following = 50 )

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


    # atividades

    """ Massive Follow de usuários seguidores (sugiro seguir não menos que
    3500/4000 usuários para melhores resultados) ...
    """
    session.follow_user_followers(['marcelo_de_brito'], amount=3500,
                                  randomize=True, interact=False)

    #Não pare de seguir usuários ativos
    """Impede os seguidores que deixaram de seguir um de seus últimos 50 posts
    """
    session.set_dont_unfollow_active_users ( enabled = True , posts = 50 )
    
    #Simulaçao
    """Durante a recuperação indireta de dados, a simulação fornece um fluxo de atividade genuíno acionado por um algoritmo inteligente.
    """
    session.set_simulation ( enabled = True , percentage = 66 )    

    #Ignorando usuário para conta particular, sem foto de perfil, conta comercial
    """Isso é usado para pular usuários com certas condições
    """
    session.set_skip_users ( skip_private = False ,
                             skip_no_profile_pic = Verdadeiro ,
                             no_profile_pic_percentage = 100 )
    
    
    # UNFOLLOW atividade
    "" " Deixar de seguir não seguidores depois de um dia ...
    "" "
    session.unfollow_users(amount=random.randint(75, 100),
                           InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=48 * 60 * 60, sleep_=600)
    #Atrasos
    """Depois de fazer cada ação, comentar, seguir ou deixar de seguir, há um atraso de sono para fornecer um fluxo de atividade suave .
    """
    session.set_action_delays(enabled=True,
                              randomize = True , 
                              random_range = ( 70 , 140 ))
                                                            

    """ Segundo passo do Massive Follow ...
    """
    session.follow_user_followers(['marcelo_de_brito'], amount=3500,
                                 randomize=True, interact=False)

    """ Juntando-se a Pods de Engajamento ...
    """
    photo_comments = ['Boa tentativa! @ {} ',
        'Impressionante! @ {} ',
        'Legal: thumbsup:',
        'Apenas incrível: open_mouth:',
        'Que câmera você usou @{}?',
        'Adore seus posts @ {}',
        'Parece incrível @{}',
        'Agradável @{}',
        ': mãos levantadas: sim!',
        'Eu posso sentir sua paixão @ {}: muscle:']

    session.set_do_comment(enabled = False, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods()
