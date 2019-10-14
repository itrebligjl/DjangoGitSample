from django.shortcuts import render

# Create your views here.
def djangogittest(request):
    return render(request, 'djangogittest.html', {})