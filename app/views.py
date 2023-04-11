from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

from django.db.models.functions import Length
def display_topics(request):
    LOT=Topics.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpages.objects.all()
    LOW=Webpages.objects.filter(TName='Cricket')
    LOW=Webpages.objects.get(TName='Cricket')
    LOW=Webpages.objects.exclude(TName='Hockey')
    LOW=Webpages.objects.all()[1:3:]
    LOW=Webpages.objects.all().order_by(Length('Cricket'))
    LOW=Webpages.objects.all().order_by('-Name')
    LOW=Webpages.objects.all().order_by('Name')
    LOW=Webpages.objects.all().order_by(Length('Name').desc())
    LOW=Webpages.objects.all()
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    
    LOA=AccessRecord.objects.filter(Date__gt='2023-10-10')
    LOA=AccessRecord.objects.filter(Date__gte='2022-10-10')
    LOA=AccessRecord.objects.filter(Date__lt='2022-10-10')
    LOA=AccessRecord.objects.filter(Date__lte='2023-6-10')
    LOA=AccessRecord.objects.all()
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)






def display_update(request):
    #TO=Topics.objects.get_or_create(TName='Bharath_Sam')[0]
    #TO.save()
    
    Webpages.objects.filter(TName='Hockey').update(Email='sbharath143@gmail.in')
    #Webpages.objects.update_or_create(TName=TO,defaults={'TName':'Bharath'})
    Webpages.objects.filter(Name='Bharath').update(TName='Cricket')
    Webpages.objects.filter(Name='Dilli').update(Email='dilli143@gmail.in')
    d={'webpages':Webpages.objects.all()}

    return render(request,'display_webpages.html',context=d)



def display_delete(request):
    Webpages.objects.filter(TName='Volley Ball').delete()

    d={'webpages':Webpages.objects.all()}

    
    return render(request,'display_webpages.html',context=d)



   