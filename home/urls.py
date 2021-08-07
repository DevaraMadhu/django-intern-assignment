from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage),
    path('delete/',views.delete_pat),
    path('update/<int:id>/',views.update_pat),
    path('create_pat/',views.create_pat),

    



]
