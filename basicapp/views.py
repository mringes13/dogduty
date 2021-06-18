from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Event

# Create your views here.
def home(request):
    allevents = Event.objects.all().filter(date=datetime.now().date()).order_by('-time')
    peecount = Event.objects.filter(activity = 'Peed', date=datetime.now().date()).count()
    poopcount = Event.objects.filter(activity = 'Poop', date=datetime.now().date()).count()
    walkcount = Event.objects.filter(activity = 'Walk', date=datetime.now().date()).count()
    eatcount = Event.objects.filter(activity = 'Eat', date=datetime.now().date()).count()
    medicinecount = Event.objects.filter(activity = 'Medicine', date=datetime.now().date()).count()
    nothingcount = Event.objects.filter(activity = 'Nothing', date=datetime.now().date()).count()
    context = {
        'events':allevents,
        'peecount':peecount,
        'poopcount':poopcount,
        'walkcount':walkcount,
        'eatcount':eatcount,
        'medicinecount':medicinecount,
        'nothingcount':nothingcount,
    }
    return render(request,'basicapp/index.html', context)

def addpee(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Peed",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged a pee.')
    return redirect('home')

def addpoop(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Poop",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged a poop.')
    return redirect('home')

def addwalk(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Walk",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged a walk.')
    return redirect('home')

def addeat(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Eat",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged a meal.')
    return redirect('home')

def addmedicine(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Medicine",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged medicine.')
    return redirect('home')

def addnothing(request):
    name = request.POST.get('name')
    now = datetime.now()
    newpeeevent = Event.objects.create(
        reporter = name, 
        activity = "Nothing",
        date = now,
        time = now)
    newpeeevent.save()
    messages.success(request, 'Successfully logged that your pet was taken out and did nothing.')
    return redirect('home')