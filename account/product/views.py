from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

def index(req):
    return render(req,'product/list.html',{"product":None})


def details(req,id):
    return render(req,'product/details.html',{"product":None})


def delete(req,id):
    #todo: delete product
    #delete product [produce:get object products - delete method]
    #if ajax : retuen message
    #if http request send : redirect
    return redirect(reverse('product:list'))


def update(req,id):
    return render(req,'product/update.html',{"product":None})