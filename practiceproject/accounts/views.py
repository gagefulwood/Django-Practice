from django.shortcuts import render

# Create your views here.

def register(request):
    if (request == 'POST'):
        pass
    else:
        return render(request,'register.html')