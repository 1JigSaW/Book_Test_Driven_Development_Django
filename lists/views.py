from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        #new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/.../')

        
    else:
        new_item_text = ''
    items = Item.objects.all()
    return render(request, 'home.html',{'items': items})

def view_list(request):
	'''represent lists'''
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
