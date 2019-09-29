from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item

# Create your views here.
def home_page(request):
    items= Item.objects.all()
    if request.method == 'POST':
      Item.objects.create(text=request.POST['item_text'])
      return redirect('/')
    return render(request, 'home.html', {'items': items})