from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    all_items = {}
    if request.method == "POST":
        #return HttpResponse(request.POST['item'])
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request, ("It has been created successfully"))
        return render(request,"index.html",{"all_items": all_items})
    else:
        all_items = List.objects.all()
        #messages.success(request, ("It has been created successfully"))
        return render(request,"index.html",{"all_items": all_items})

   