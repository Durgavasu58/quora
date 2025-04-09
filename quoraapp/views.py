from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import  *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.urls import  reverse
from .models import *
from django.db.models import Q

def home(request):
    """
        Display the all questions, ordered by latest.
    """
    questions = Question.objects.all().order_by('-id')
    context = {
        "questions":questions
    }

    return  render(request,"quoraapp/home.html", context)

def index(request):
    return render(request,"base.html")

def user_register(request):
    """
        Handling the user registration. validating and saving user, then redirecting to the login Page.
    """

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user)
            return redirect("quoraapp:login_view")
    return  render(request, "quoraapp/register.html")

def userlogin(request):
    """
        Handling the  user login using either username or email.
        - If already authenticated, redirecting to home.
        - On POST: authenticating and login the user.
    """
    if request.user.is_authenticated:
        return  redirect("quoraapp:home_view")

    error = None
    if request.method == 'POST':
        login_input  = request.POST['username']
        password = request.POST['password']
        print(login_input,password)
        try:
            user_obj = User.objects.get(Q(username=login_input) | Q(email=login_input))
            user = authenticate(request, username=user_obj.username, password=password)

            print("Authenticated user:", user)
            if user:
                login(request, user)
                return redirect("quoraapp:home_view")
            else:
                error = "Invalid Credentials"
        except User.DoesNotExist:
            error = "Enter your Credentials"

    return render(request, "quoraapp/login.html", {'error': error})

@login_required()
def user_logout(request):
    logout(request)
    return redirect("quoraapp:home_view")

@login_required()
def ask_question(request):
    """
        Allow an authenticated user to post a new question.
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author_name = request.user
            question.save()
            return  redirect("quoraapp:home_view")
    return  render(request, "quoraapp/question.html")

def question_detail(request, id):
    """
        Display details of a question :
        - Full question content
        - Likes
        - Comments
        Also handling POST to add a comment if the user is authenticated only.
    """

    indivigual_question = get_object_or_404(Question,id=id)


    if indivigual_question.likes.filter(id=request.user.id).exists():
        question_like = True
    else:
        question_like = False

    user_comments = Comments.objects.filter(question_id=id).order_by("-id")

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("quoraapp:login_view")

        contact = CommentForm(request.POST)
        if contact.is_valid():
            comment_save = contact.save(commit=False)
            comment_save.user = request.user
            comment_save.question = indivigual_question
            comment_save.save()
            return  redirect("quoraapp:question_detail_view", id=id)
    context = {
        "indivigual_question":indivigual_question,
        "question_like":question_like,
        "user_comments":user_comments
    }
    return render(request, "quoraapp/question_detail.html", context)

def question_like(request):
    if not request.user.is_authenticated:
        return  redirect("quoraapp:login_view")
    like_ques = get_object_or_404(Question, id=request.POST.get("indivigual_question_id"))
    print("like_ques",like_ques,request.POST.get("indivigual_question_id"))

    if like_ques.likes.filter(email=request.user.email).exists():
        like_ques.likes.remove(request.user)
    else:
        like_ques.likes.add(request.user)

    return redirect("quoraapp:question_detail_view" ,id=request.POST.get("indivigual_question_id"))