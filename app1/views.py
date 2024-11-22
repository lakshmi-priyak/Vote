from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vote

def index(request):
    members = Vote.objects.all()
    template = loader.get_template('vote.html')
    context = {
        'members' : members,
    }
    return HttpResponse(template.render(context,request))