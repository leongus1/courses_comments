from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_course),
    path('courses/destroy/<int:course_id>', views.remove_course_page),
    path('courses/destroy/<int:course_id>/delete', views.confirm_remove),
    path('courses/<int:course_id>', views.edit),
    path('courses/<int:course_id>/update', views.update)
    
]