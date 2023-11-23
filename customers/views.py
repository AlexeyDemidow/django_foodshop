from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from customers.forms import CustomerCreationForm
from customers.models import Customer


class SignUpView(CreateView):
    """Представление регистрации пользователя"""

    form_class = CustomerCreationForm
    success_url = reverse_lazy('signup_success')
    template_name = 'registration/signup.html'


class SignUpSuccess(TemplateView):
    """Представление успешной регистрации пользователя"""

    template_name = 'registration/signup_success.html'


class Login(LoginView):
    """Представление входа в систему"""

    form_class = AuthenticationForm
    success_url_allowed_hosts = reverse_lazy('home')
    template_name = 'registration/login.html'


class Profile(LoginRequiredMixin, DetailView):
    """Представление профиля пользователя"""

    model = Customer
    template_name = 'customer_profile.html'
    context_object_name = 'customer'

    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):
    """Представление обновления данных профиля пользователя"""

    model = Customer
    fields = ['customer_name', 'telephone', 'date_of_birth']
    template_name = 'update_profile.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('customer_profile', kwargs={'pk': pk})
