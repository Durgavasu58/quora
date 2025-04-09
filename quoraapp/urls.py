from django.urls import path
from . import  views

app_name = "quoraapp"

urlpatterns = [
    path('',views.home,name="home_view"),
    path('login/',views.userlogin, name="login_view"),
    path('register/',views.user_register, name="register_view"),
    path('logout/',views.user_logout, name = "logout_view"),
    path('question/',views.ask_question, name="question"),
    path('question_detail/<int:id>', views.question_detail, name="question_detail_view"),
    path('questionlikes/',views.question_like, name="like_view")

]
