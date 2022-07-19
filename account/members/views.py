from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def halo(req):
    return HttpResponse(' hello user ')


def log(req):
    return HttpResponse(' you loggeed in ')


def logt(req):
    return HttpResponse(' you loggecd out')


def user(req,id):
    return  HttpResponse('user:'+str(id))