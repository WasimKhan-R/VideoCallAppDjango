from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')

def videacall(request):
    return render(request, 'WEB_UIKITS.html')