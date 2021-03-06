from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('detail/', AgentDetailView.as_view(), name='agent-detail'),
]