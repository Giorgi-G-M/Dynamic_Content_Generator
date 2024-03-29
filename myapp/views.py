from django.shortcuts import render, redirect

# Create your views here.


def words(request):
    return render(request, 'myapp/page.html')


def function(request):
    if request.method == "POST":
        user = (dict(request.POST.items()))
        return render(request,'myapp/page.html',{"Name":user})
    return render(request, 'myapp/index.html')
    
