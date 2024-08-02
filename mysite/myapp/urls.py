from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/myapp/hello/
    path('', views.index, name='index'),


    path('<int:my_id>/', views.indexItem, name='detail'),
    

    #http://127.0.0.1:8000/myapp/contacts/
    
    path('additem/', views.add_item, name='add_item'),

    path('updateitem/<int:my_id>/', views.update_item, name='update_item'),
    path('deleteitem/<int:my_id>/', views.delete_item, name='delete_item'),
    ]
