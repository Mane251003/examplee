from django.shortcuts import render
from .problem import problem
def home(request):
    result=None
    if request.method=='POST':
        result=problem()

    context = {
        'result': result,
    }
    return render(request, 'home.html', context)


def result(request):
    p = problem()
    context = {
        'result': p,
    }
    return render(request, 'result.html', context)