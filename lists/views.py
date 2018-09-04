from django.shortcuts import render
from lists.models import Item
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
# @csrf_exempt
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''
    #     item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    return render(request, 'home.html', {
        'new_item_text': new_item_text,
    })


