from django.shortcuts import render
from getScores import getScore
from scraping import scrape
from django.shortcuts import redirect

# Create your views here.
def home(request):
        return render(request , 'index/home.html')
    


def ranked(request):
    if request.method == 'POST':
        linkr1 = request.POST.get('link1' ,False)
        linkr2 = request.POST.get('link2' ,False)
        linkr3 = request.POST.get('link3' ,False)
        try:
            link1= getScore(linkr1)
        except:
            return redirect('/error')
        try:
            link2= getScore(linkr2)
        except:
            return redirect('/error')
        try:
            link3= getScore(linkr3)
        except:
            return redirect('/error')

        print('name:')
        context= {
            round(link1,3) : linkr1,
            round(link2,3) : linkr2,
            round(link3,3) : linkr3,
        }
        
    else :
        return render(request , 'index/home.html')
    return render(request , 'index/ranked.html' ,{'data' : reversed(sorted(context.items()))})

def about(request):
    return render(request , 'index/about.html')

def error(request):
    return render(request , 'index/error.html') 

