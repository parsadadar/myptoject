from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

vips={
    'a21':'stiv_jobs',
    'b32':'bill_gates',
    'c54':'ahmad_zoqi',
    'd18':'parsa_dadar',
    'e13':'jeyzi',
}



def special_num(req,cod):
    vip_codd = list(vips.keys())
    if cod > len(vip_codd):
        return HttpResponseNotFound('this code is not exists.')
    redirect_vip = vip_codd[cod - 1]
    redirect_url = reverse('010123', args=[redirect_vip])
    return HttpResponseRedirect(f'/vip/{redirect_vip}')


def spec(req):
    vip_list=list(vips.keys())
    context={
        "vips":vip_list
    }
    return render(req,'members/vips.html',context)

def adm(req):
    return render(req,'members/admin_site.html')

def special(req,cod):
    vip_cd=vips.get(cod)
    if vip_cd is None:
        response_data=render_to_string('erors/404.html')
        return HttpResponseNotFound(response_data)
    context={
        'data': f'vip id is {vip_cd}',
        'cod':f'vip cod is {cod}',
    }
    return render(req,'members/helo.html',context)





































