from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ismart/', views.ismart, name='ismart'),
    path('goal-list/', views.GoalListView.as_view(), name='goal_list'),
    path('goal-list/my-goal/<int:pk>', views.GoalDetailView.as_view(), name='goal_detail'),
    path('create-goal/', views.GoalCreateView.as_view(), name='create_goal'),
] 