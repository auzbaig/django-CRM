from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
#from django.http.response import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import generic
#from django.http import HttpRequest
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm#, AssignAgentForm

# CRUD + L - Create, Retrieve, Update and Delete + List

class SignupView(generic.CreateView):
    template_name  = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, 'landing.html')

def lead_list(request):
    #return HttpResponse("Hello world")
    #return render(request,'leads/home_page.html')
    
    leads = Lead.objects.all() #leads is now a list of the returned query set

    context={ 'leads' : leads}
    return render(request,'leads/lead_list.html', context)

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    #queryset = Lead.objects.all(), now we will filter the query set
    context_object_name = "leads"

    def get_queryset(self):
        queryset = Lead.objects.all()
        if self.request.user.is_agent:
            queryset = queryset.filter(agent__user=self.request.user) #filter the leads based on the agent field where that agent has the user = self.request user
        return queryset

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead' : lead
    }
    return render(request, 'leads/lead_detail.html', context)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name  = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/leads')

    context = {
        'form' : form
    }
    return render(request, 'leads/lead_create.html', context)

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name  = "leads/lead_create.html"
    #queryset = LeadModelForm()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        #TODO sed email
        send_mail(
            subject="Subject",
            message="Go to site",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)



def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'lead' : lead,
        'form' : form
    }

    return render(request, 'leads/lead_update.html', context)

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name  = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:lead-list")

"""
class AssignAgentView(LoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = None #AssignAgentForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    #have to implement the form valid method to save it
"""
"""
def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()

            Lead.objects.create(
            first_name = first_name,
            last_name = last_name,
            age=age,
            agent=agent
            )

            return redirect('/leads')

    context = {
        'form' : form
    }
    return render(request, 'leads/lead_create.html', context)
"""