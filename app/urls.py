
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path("", views.index,name="home"),
    path("about", views.about,name="about"),
    path("contact", views.contact,name="contact"),
    path("login", views.loginUrl,name="login"),
    path("logout", views.logoutUrl,name="logout"),
    path("addUser", views.addUser,name="addUser"),
    path("userAdded/", views.userAdded,name="userAdded"),
    path("login_req/", views.login_req,name="login_req"),
    path("submit", views.submit,name="submit"),
    path("view", views.view,name="view"),
    path("submitted/", views.submitted,name="submitted"),
]  