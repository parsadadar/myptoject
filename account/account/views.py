from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(req):
    return HttpResponse("index page...")