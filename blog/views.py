from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #三个参数1 request， 2、Templates（html）路径 3 、参数{dict}
    return render(request, 'index.html', {'hello': 'Hello, Blog!'})
