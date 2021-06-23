from django.urls import path
from .views import (
    todo_detail,
    todo_list , 
    todo_create,
    todo_update,
    todo_delete
)

app_name = 'todos'

urlpatterns = [
    path('' , todo_list),
    path('create/' , todo_create),
    path('<id>/update/' , todo_update),
    path('<id>/delete/' , todo_delete),
    path('<id>/' , todo_detail),
]   
    
