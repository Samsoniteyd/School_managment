from django.urls import path
from. import views

urlpatterns = [
    path('', views.all_category, name='all_category'),
    path('category_question/<int:cat_id>/', views.category_question, name='category_question'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer, name='submit_answer'),
]