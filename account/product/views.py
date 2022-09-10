from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from datetime import datetime
from .models import products, category, subcategory
from django.views.generic import TemplateView, View, DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator

class ClassIndex(TemplateView):
    template_name = "product/list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pros = products.objects.all()
        context['products'] = pros
        return context

    def get(self, request, *args, **kwargs):
        print(args, kwargs, request.GET)
        return render(request, self.template_name, self.get_context_data(**kwargs))

class ClassViewIndex(View):
    template_name = "product/list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        pros = products.objects.all()
        context['products'] = pros
        return render(request, self.template_name, context)


class ClassDetails(DetailView):
    model = products


    def get_template_names(self):
        return "product/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = datetime.now()
        return context


class ClassList(ListView):
    model = products
    paginate_by = 5
    page_kwarg = "dadar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = datetime.now()
        return context


def index(req):
    pros = products.objects.get_queryset().order_by('id')
    paginator = Paginator(pros, 5)
    page_number = req.GET.get('dadar')
    page_obj = paginator.get_page(page_number)
    return render(req, 'product/list.html', {"products": pros, 'page_obj': page_obj})



def details(req,id):
    try:
        pro = products.objects.get(id=id)
    except products.DoesNotExist:
        return HttpResponse("Error")
    if req.method == "GET":
        return render(req, "product/details.html", {"product": pro})
    else:
        return Http404

def delete(req,id):
       pro = products.objects.get(id=id).delete()
       return render(req, "product/list.html", {"product":pro})



def delete_noajax(req, id):
    try:
        pro = products.objects.get(id=id).delete()
        return render(req, "product/delete_noajax.html", {"product": pro})
    except products.DoesNotExist:
        return redirect(reverse("product:list"))


def update(req,id):
    try:
        pro = products.objects.get(id=id)
    except products.DoesNotExist:
        return HttpResponse("Error")
    if req.method == "GET":
        return render(req, "product/update.html", {"product": pro})
    elif req.method == "POST":
        name = req.POST.get("name", False)
        count = req.POST.get("count", False)
        amount = req.POST.get("amount", False)
        pro.name = name
        pro.count = count
        pro.amount = amount
        pro.save()
        return redirect(reverse("product:list"))
    else:
        return Http404

def ebook(req):
    pros = products.objects.all()
    paginator = Paginator(pros, 5)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req, 'product/index.html', {'products':pros,'page_obj':page_obj})

def all_book(req):
    pros = products.objects.all()
    paginator = Paginator(pros, 6)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req, 'product/list_book.html',{'products':pros,  'page_obj':page_obj})