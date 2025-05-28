from django.shortcuts import render
from .problem import problem
def home(request):
    p=problem()
    print(p)
    context = {
        'problem': p,
    }
    return render(request, 'home.html', context)

def result(request):
    p = problem()
    context = {
        'result': p,
    }
    return render(request, 'result.html', context)