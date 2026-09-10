from django.shortcuts import render
from .models import user


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        student = user.objects.get(
            username=username,
            password=password
        )

        return render(request,"profile.html", {"student": student})

    return render(request, "login.html")
