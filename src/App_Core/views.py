from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'base.html' )

def loginPage(request):
    return render(request, 'login.html')
