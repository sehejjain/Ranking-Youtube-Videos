from django.shortcuts import render
from getScores import getScore
from scraping import scrape

# Create your views here.
def home(request):
    if request.method == 'POST':
        linkr1 = request.POST.get('link1' ,False)
        linkr2 = request.POST.get('link2' ,False)
        linkr3 = request.POST.get('link3' ,False)
        link1= 3
        link2 = 2
        link3 = 5
        l1name = scrape(linkr1)
        print('name:')
        print(l1name)
        context= {
            link1 : linkr1,
            link2 : linkr2,
            link3 : linkr3,
        }
        
    else :
        return render(request , 'index/home.html')
    return render(request , 'index/home.html' ,{'data' : sorted(context.items())})