from django.shortcuts import render
from getScores import getScore
from scraping import scrape

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
            link1 = 3
        try:
            link2= getScore(linkr2)
        except:
            link2 = 1
        try:
            link3= getScore(linkr3)
        except:
            link3 = 4

        print('name:')
        context= {
            link1 : linkr1,
            link2 : linkr2,
            link3 : linkr3,
        }
        
    else :
        return render(request , 'index/home.html')
    return render(request , 'index/ranked.html' ,{'data' : sorted(context.items())})

def about(request):
    return render(request , 'index/about.html')
