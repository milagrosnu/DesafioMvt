from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppMvt.models import People

# Create your views here.
def people(request):

    person1 = People(name='Mariela', last_name='Lopez', age=30, birthday= '1992-08-12')
    person2 = People(name='Juan', last_name='Lopez', age=10, birthday= '2012-10-22')
    person3 = People(name='Luna', last_name='Lopez', age=32, birthday= '1990-04-20')

    people_list = [person1, person2, person3]
    
    for everyone in people_list:
        everyone.save()

def list(request):
    
    list = People.objects.all()
    return render(request, 'people.html', {'list':list})


