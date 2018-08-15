# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.db.models import Avg ,Q
# Create your views here.
def get_playerAvgAge(req):
    players=player.objects.filter(team__name="国家队")
    res=players.aggregate(Avg("age"))
    print (res)
    return HttpResponse(json.dumps(res))

def get_team(req):
    data=Team.objects.raw("select * from t03_team")
    return  render(req,"teams.html",{"teams":data})
def get_players_by_tid(req):
    param=req.GET
    t_id = param.get("tid")
    res=player.objects.filter(
        team_id=int(t_id)
    )
    return render(req,"players.html",{"players":res})

def getIDcardBYperson(req):
    p = Person.objects.all().last()
    my_card=p.idcard
    print(my_card)
    return HttpResponse(my_card.num)

def getPersonBYcard(req):
    card=IdCard.objects.get(pk=1)
    p=card.person
    print(type(p))
    #让对象转成字典
    res=model_to_dict(p)
    print(type(res))
    return HttpResponse(json.dumps(res))

def deletePerson(req):
    person=Person.objects.get(id=2).last()
    person.delete()
    return HttpResponse("ok")

def delete_card(req):
    card=IdCard.objects.all().first()
    card.delete()
    return HttpResponse("oook")

def getPlayerbyTEAM(req):
    team=Team.objects.get(pk=1)
    players =team.player_set.all()
    # print(dir(players))
    # res=[model_to_dict(i) for i in players]
    return HttpResponse(players)

def getAUTHORbyBook(req):
    book=Book.objects.get(pk=1)
    print(dir(book.author))
    print(book.author.all())
    return HttpResponse("ok")

def getbookBYAUthor(req):
    author=Author.objects.get(id=1)
    res=author.book_set.all()
    return HttpResponse(res)