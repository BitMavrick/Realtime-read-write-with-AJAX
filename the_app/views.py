from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import data

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def createData(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']

        new_data = data(name=name, age=age)
        new_data.save()

        return HttpResponse('Create successfully!')

def view_data(request):
    return render(request, 'view.html')

def getData(request):
    all_data = data.objects.all()

    return JsonResponse(
        {
            'data' : list(all_data.values())
        }
    )
