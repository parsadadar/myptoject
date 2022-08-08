from multiprocessing import context
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


vips={
    'a':'stiv_jobs',
    'b':'bill_gates',
    'c':'ahmad_zoqi',
}


def special_num(req,cod):
    vip_codd = list(vips.keys())
    if cod > len(vip_codd):
        return HttpResponseNotFound('this code is not exists.')
    redirect_vip = vip_codd[cod - 1]
    redirect_url = reverse('010123', args=[redirect_vip])
    return HttpResponseRedirect(f'/vip/{redirect_vip}')


def special(req,cod):
    vip_found=vips.get(cod)
    if vip_found is not None:    
        context={
            "data":vip_found
        }
        return render(req,"members/vips.html",context)
    return HttpResponseNotFound('not found, try another vip code.')

def adm(req):
    return render(req,'members/member.html')