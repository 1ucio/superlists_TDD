from django.shortcuts import render, redirect
from lists.models import Item, List
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
# @csrf_exempt
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
    return redirect('/lists/%d/' % (list_.id,))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
    return redirect('/lists/%d/' % (list_.id,))


