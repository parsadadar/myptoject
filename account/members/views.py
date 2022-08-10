from multiprocessing import context
import re
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
    if vip_cd is not None:
        context={
            'data': f'COD {cod}',
            'cod':f'vip cod is for {vip_cd}',
        }
        return render(req,'members/helo.html',context)