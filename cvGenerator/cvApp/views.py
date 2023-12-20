from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def acceptView(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        university = request.POST.get("university","")
        degree = request.POST.get("degree","")
        high_school = request.POST.get("high_school","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
        
        profile = Profile(name = name, email = email, phone = phone, summary = summary, university = university,degree = degree, high_school = high_school, previous_work = previous_work, skills = skills)
        profile.save()
        
    return render(request,'accept.html')

def cvView(request,id): 
    user_profile = Profile.objects.get(pk = id)
    template = loader.get_template('cv.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "cv.pdf"
    return response

def listView(request):
    profiles = Profile.objects.all()
    return render(request,'list.html',{'profiles':profiles})