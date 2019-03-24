from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from openforce_app.models import ratings


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/openforce/mainpage")

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/openforce/")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def mainpage(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/openforce/")

    context = {
        'sessionID': request.session.session_key
    }

    return render(request, 'mainpage.html', context)


def saveDB(request):
    print("Views save db");
    ratingsObj = ratings()
    ratingsObj.rating = request.GET.get('rating')
    ratingsObj.quote = request.GET.get('quote')
    ratingsObj.session = request.GET.get('session')
    ratingsObj.username = request.GET.get('uname')

    print(f"To Save | {ratingsObj.username} | {ratingsObj.quote} | {ratingsObj.session} | {ratingsObj.rating} |")

    ratingsObj.save()
    return render(request, 'mainpage.html')


def getRatingsDB(request):
    ratingsRow = ratings.objects.all().filter(quote=request.GET.get('quote'))
    avgrate = 0
    for r in ratingsRow:
        avgrate += r.rating

    avgrate /= len(ratingsRow)
    isRated = False

    isRatedList = ratings.objects.all().filter(quote=request.GET.get('quote'), username=request.GET.get('uname'),
                                           session=request.GET.get('session'))
    if isRatedList:
        isRated = True

    print(f"Testing RateDB | {avgrate} | {isRated} |")
    context = {
        'avgrating': avgrate,
        'israted': isRated
    }

    return render(request, 'mainpage.html', context)
