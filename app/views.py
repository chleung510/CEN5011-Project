"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from app.models import Notice
from .forms import CreateNoticeForm



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    noticedata = Notice.objects.all()
    query = request.GET.get('q')
    if(query and len(query) > 0):
        noticedata=Notice.objects.filter(heading__icontains=query)

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        noticedata = Notice.objects.filter(
            Q(heading__icontains=query) | Q(content__icontains=query)
        )

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'noticedata':noticedata
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Contact address.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Neighborhood',
            'message':'A social media application based on your location.',
            'year':datetime.now().year,
        }
    )


def createnotice(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    form = CreateNoticeForm()
    if request.method == "POST":        
        form = CreateNoticeForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/')
    noticedata = Notice.objects.all()
    return render(
        request,
        'app/createnotice.html',
        {
            'title':'Create Notice',          
            'year':datetime.now().year,
            'noticedata':noticedata,
            'form': form
        }
    )


def updatenotice(request,pk):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    notice = Notice.objects.get(noticeID=pk)
    form = CreateNoticeForm(instance=notice)
    if request.method == "POST":        
        form = CreateNoticeForm(request.POST, instance=notice)
        if form.is_valid():
                form.save()
                return redirect('/')
    noticedata = Notice.objects.all()
    return render(
        request,
        'app/updatenotice.html',
        {
            'title':'Update Notice',          
            'year':datetime.now().year,
            'noticedata':noticedata,
            'form': form
        }
    )


def deletenotice(request,pk):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    notice = Notice.objects.get(noticeID=pk)   
    if request.method == "POST":        
        notice.delete()
        return redirect('/')        
  
    return render(
        request,
        'app/deletenotice.html',
        {
            'title':'Delete Notice',          
            'year':datetime.now().year,           
            'notice': notice
        }
    )
