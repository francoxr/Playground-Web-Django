from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

from .models import Profile
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm


# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        """change atributes for form"""
        form = super(SignupView, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Direccion Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contrasena'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contrasena'})
        return form

class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html' 

    def get_object(self):
        """Return to user's profile"""

        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html' 

    def get_object(self):
        """Recuperar el objeto que se va editar"""

        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form(form_class)
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form