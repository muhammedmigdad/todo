from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
   path("", views.index, name="index"),
   path("login/", views.login, name="login"),
   path("register/", views.register, name="register"),
   path("logout/", views.logout, name="logout"),
   path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
   path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
   path('todo_done/<int:id>/', views.todo_done, name='todo_done'),
]