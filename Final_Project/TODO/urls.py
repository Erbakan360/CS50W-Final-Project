from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("edit_task", views.edit_task, name="edit_task"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("view_task", views.view_task, name="view_task"),
    path("Copy_task", views.Copy_task, name="Copy_task"),
    path("create_task", views.create_task, name="create_task"),
    path("remove_task", views.remove_task, name="remove_task"),
    path("task_complete", views.task_complete, name="task_complete"),
    path("complete_tasks", views.complete_tasks, name="complete_tasks"),
]