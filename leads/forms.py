from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username' : UsernameField}

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

#class AssignAgentForm(forms.Form):
    #ChoiceField and ModelChoiceField
    #agent = forms.ChoiceField(choices=(
    #        ("agent 1", "agent 1"),
    #      ("agent 2", "agent 2"),
    #        ))
 #   agent = forms.ModelChoiceField(queryset=Agent.objects.none())

   # def __init__(self, *args, **kwargs):
