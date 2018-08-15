from django.conf.urls import url
from .views import *


urlpatterns=[
    url(r"^get_player_v1$",get_playerAvgAge),
    url(r'^team$',get_team),
    url(r'^players$',get_players_by_tid),
    url(r'^getcard$',getIDcardBYperson),
    url(r'^getperson$',getPersonBYcard),
    url(r'^delperson$',deletePerson),
    url(r'^delcard$',delete_card),
    url(r'^getplayersbyt$',getPlayerbyTEAM),
    url(r'^getauthor$',getAUTHORbyBook),
    url(r'^getbook$',getbookBYAUthor)
]