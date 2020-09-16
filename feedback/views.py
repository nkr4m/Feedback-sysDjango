from django.shortcuts import render, HttpResponse
from feedback.models import Feedback
from datetime import datetime

def index(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        feed = Feedback(name = name, email = email, phone = phone, date = datetime.today())
        feed.save()

    return render(request, 'index.html')

