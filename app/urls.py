from django.urls import path

from app.views import index_view, add_view, detail_view, delete_view, add_student_view, edit_student_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add'),
    path('add-student/', add_student_view, name='add-student'),
    path('student/<int:student_id>/', detail_view, name='student'),
    path('delete/<int:student_id>/', delete_view, name='delete'),
    path('edit-student/<int:student_id>/', edit_student_view, name='edit'),

]