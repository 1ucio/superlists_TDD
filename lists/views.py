from django.shortcuts import render, redirect
from lists.models import Item, List
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
# @csrf_exempt
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
    return redirect('/lists/the-only-list-in-the-world/')


