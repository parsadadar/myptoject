from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import  datetime
from .models import products,category,subcategory
from django.views.generic import TemplateView, View, DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator

class ClassIndex(TemplateView):
    template_name = "product/list.html"
    # http_method_names = ["get"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pros = products.objects.all()
        context['products'] = pros  # you want to set Object Model, if you can.
        return context

    def get(self, request, *args, **kwargs):
        print(args, kwargs, request.GET)
        # self.template_name
        return render(request, self.template_name, self.get_context_data(**kwargs))

class ClassViewIndex(View):
    template_name = "product/list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        pros = products.objects.all()
        context['products'] = pros  # you want to set Object Model, if you can.
        # print(args, kwargs, request.GET)
        # self.template_name
        return render(request, self.template_name, context)


class ClassDetails(DetailView):
    model = products

    # if you want change template name
    def get_template_names(self):
        return "product/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = datetime.now()
        return context


class ClassList(ListView):
    model = products
    paginate_by = 5  # if pagination is desired
    page_kwarg = "dadar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = datetime.now()
        return context


def index(req):
    pros = products.objects.all()
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
        # todo: delete product
        # delete product [produce:get object Products - delete method]
        # if ajax : return message
        # if http request send : redirect [list]

        # print(req.is_ajax())
        # return HttpResponse("OK")

        try:
            pros = products.objects.get(id=id)
            pros.delete()
            if req.is_ajax():
                return HttpResponse("OK")
            else:
                return redirect(reverse("product:list"))
        except products.DoesNotExist:
            if req.is_ajax():
                return HttpResponse("Error")
            else:
                return redirect(reverse("product:list"))
        # return redirect(reverse("product:list"))


def delete_noajax(req, id):
    # todo: delete product
    # delete product [produce:get object Products - delete method]
    # if ajax : return message
    # if http request send : redirect [list]
    try:
        pro = products.objects.get(id=id)
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