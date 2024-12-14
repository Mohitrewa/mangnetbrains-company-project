from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('', TemplateView.as_view(template_name="index.html")), # type: ignore
]