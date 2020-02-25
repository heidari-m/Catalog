from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'quick': 1,
               'start': 2}
    return render(request, 'seed/init.html', context=context)
