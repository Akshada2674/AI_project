from django.shortcuts import render , HttpResponse

def home_page(request):
    return render(request ,"base.html")

def getResponse(request):
     userMessage = request.GET.get('userMessage')
     return HttpResponse(userMessage)