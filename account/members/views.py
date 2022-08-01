from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
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
    redirect_url = reverse('010123', lis=[redirect_vip])
    return HttpResponseRedirect(f'/vip/{redirect_vip}')


def special(req,cod):
    vip_found=vips.get(cod)
    if vip_found is not None:    
        response_data = f'<h1 style="color:blue">user:{cod} is {vip_found}</h1>'
        return HttpResponse(response_data)
    return HttpResponseNotFound('not found, try another vip code.')