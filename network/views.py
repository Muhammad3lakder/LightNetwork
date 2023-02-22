from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, follow
from django.core.paginator import Paginator
import json


def index(request):

    # User reached route via POST
    if request.method == 'POST':
        content = request.POST['content']
        user = User.objects.get(pk=request.user.id)

        # Check if user has submitted a form and save into the DB
        if content:
            Submit = Post.objects.create(content=content, author=user)
            Submit.save()

            # Redirect user to index page
            return HttpResponseRedirect(reverse("index"))

    # User reached route via GET
    else:

        # Query all the posts from the DB
        AllPosts = Post.objects.all().order_by("date").reverse() 

        # Show 10 posts per page
        paginator = Paginator(AllPosts, 10)

        page_number = request.GET.get('page')
        paginator_obj = paginator.get_page(page_number)

        # Check if there is any posts yet
        if paginator_obj:
            return render(request, "network/index.html", {
                "allposts":paginator_obj
            })

        return render(request, "network/index.html")
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile(request, username):

    # User reached route via GET

    # Queryset for user`s data from the DB
    profile = User.objects.get(username=username)

    # Query all the posts from the DB
    AllPosts = Post.objects.filter(author=profile).order_by("date").reverse() 

    # Show 10 posts per page
    paginator = Paginator(AllPosts, 10)

    page_number = request.GET.get('page')
    paginator_obj = paginator.get_page(page_number)

    # Query for number of following
    following_count = follow.objects.filter(follower=profile)

    print(following_count)
    # Query for number for follower for this user
    followers = follow.objects.filter(following=profile)

    # Check if logged in user is following this user or not
    check_for_follow = follow.objects.filter(
        follower=User.objects.get(pk=request.user.id)
    )

    if len(check_for_follow) >= 1:
        check_for_follow = True
    else:
        check_for_follow = False

    # Check if there is any posts yet
    if paginator_obj:
        return render(request, "network/profile.html", {
            "allposts": paginator_obj,
            "username": username, 
            "following": following_count,
            "followers": followers,
            "check_for_follow": check_for_follow
        })


@csrf_exempt
def edit(request, post_id):

    # User must reach this route via POST
    if request.method != 'POST':
        return JsonResponse({"error: POST request required."}, status=400)

    # Check submitted post
 


    data = json.loads(request.body)
    edit_post = Post.objects.get(pk=post_id)
    edit_post.content = data["content"]
    edit_post.save()

    return JsonResponse({"message": "Post edited successfully"}, status=201)