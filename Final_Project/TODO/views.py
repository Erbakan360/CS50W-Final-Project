from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Task
from datetime import datetime
# Create your views here.

@login_required
def index(request):
    if request.POST.get("Search") != None:
        return render(request, ("TODO/index.html"), {
            "Tasks": Task.objects.all().filter(Task_user = User.objects.get(username = request.user)).filter(Status = False).order_by(request.POST.get("Search")),
            })
    else:
        return render(request, ("TODO/index.html"), {
            "Tasks": Task.objects.all().filter(Task_user = User.objects.get(username = request.user)).filter(Status = False),
            })

@login_required
def view_task(request):
    id = request.POST.get("id")
    Tasks = Task.objects.all().filter(pk = id)
    return render(request, ("TODO/view.html"), {"Tasks":Tasks})

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, ("TODO/create.html"))
    else:
        Title = request.POST.get("Title")
        Content = request.POST.get("Desc")
        Deadline = request.POST.get("Deadline")
        Categories = request.POST.get("Categories")
        Status = request.POST.get("Status")
        time = datetime.today().replace(microsecond=0),

        if Title == None or Title == "" or Content == None or Content == "" or len(Deadline) == 0 or Categories == None or Categories == "":
            return render(request, ("TODO/create.html"), {"error": "Please input values in all fields"})
        else:
            if Deadline == "":
                Deadline = None 
            if Status == None or Status == "":
                Status = False
            
            add_Task = Task(
                Task_user = User.objects.get(username = request.user),
                Task_Title = Title,
                Task_Content = Content,
                Task_Flag = Categories,
                start_time = time,
                deadline = Deadline,
                Status = Status,
            )
            add_Task.save()
    return redirect("index")

@login_required
def edit_task(request):
    Tasks = Task.objects.all().filter(pk = request.POST.get("id"))
    return render(request, ("TODO/edit.html"), {"Tasks": Tasks})

@login_required
def save_edit(request):
    Title = request.POST.get("Title")
    Content = request.POST.get("Desc")
    Deadline = request.POST.get("Deadline")
    Categories = request.POST.get("Categories")
    Status = request.POST.get("Status")

    if Title == None or Title == "" or Content == None or Content == "" or Categories == None or Categories == "":
        Tasks = Task.objects.all().filter(pk = request.POST.get("id"))
        return render(request, ("TODO/edit.html"), {"Tasks": Tasks, "error": "Please input values in all fields"})
    else:
        Tasks = Task.objects.get(id = request.POST.get("id"))
        if Status == None or Status == "":
            Status = Tasks.Status
        if Deadline == None or Deadline == "":
            Deadline = Tasks.deadline
        Tasks.Task_Title = Title
        Tasks.Task_Content = Content
        Tasks.deadline = Deadline
        Tasks.Task_Flag = Categories
        Tasks.Status = Status
        Tasks.save()
    return redirect("index")

@login_required
def remove_task(request):
    Tasks = Task.objects.get(pk = request.POST.get("id"))
    Tasks.delete()
    return redirect("index")

@login_required
def task_complete(request):
    Tasks = Task.objects.get(pk = request.POST.get("id"))
    if Tasks.Status == False:
        Tasks.Status = True
        Tasks.save()
    else:
        Tasks.Status = False
        Tasks.save()
    return redirect("index")

@login_required
def complete_tasks(request):
    return render(request, ("TODO/index.html"), {
        "Tasks": Task.objects.all().filter(Task_user = User.objects.get(username = request.user)).filter(Status = True),
        })

def Copy_task(request):
    Tasks = Task.objects.get(pk = request.POST.get("id"))
    time = datetime.today().replace(microsecond=0),
    Duplicate = Task(
        Task_user = Tasks.Task_user,
        Task_Title = Tasks.Task_Title + " - Duplicate",
        Task_Content = Tasks.Task_Content,
        Task_Flag = Tasks.Task_Flag,
        start_time = time,
        deadline = Tasks.deadline,
        Status = Tasks.Status,
    )
    Duplicate.save()
    return redirect("index")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ LOGIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "TODO/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "TODO/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "TODO/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "TODO/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "TODO/register.html")