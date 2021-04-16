from django.shortcuts import reverse
from django.views import generic
#from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import OrganizerAndLoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
# Create your views here.

class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        #return Agent.objects.all() #if you don't want to filter by organization
        organization = self.request.user.userprofile  #filtering by organization Foreign Key
        return Agent.objects.filter(organization = organization)


class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name  = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self,form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin , generic.DetailView):
    template_name = "agents/agents_detail.html"

    def get_queryset(self):
        return Agents.objects.all()