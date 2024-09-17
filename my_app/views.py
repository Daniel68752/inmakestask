from django.shortcuts import render
from .models import  Portfolio,Portfolio2,PortfolioEdu

# Create your views here.



def Index(request):
    prtfolio=Portfolio.objects.all()
    prtfolio2=Portfolio2.objects.all()
    prtfolio3=PortfolioEdu.objects.all()
    return render(request,'index.html',{'prtfolio':prtfolio,'prtfolio2':prtfolio2,'prtfolio3':prtfolio3})
