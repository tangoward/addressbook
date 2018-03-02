from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import ContactPerson
from .forms import UserCreateForm
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('contacts:login')
    template_name = 'contacts/signup.html'


class ProfileView(ListView):
    model = ContactPerson
    template_name = 'contacts/profile.html'
    queryset = ContactPerson.objects.all()

    def get_queryset(self):
        return self.queryset.filter(contact_owner=self.request.user)


class ThanksView(TemplateView):
    template_name = 'contacts/thanks.html'


class CreateContact(CreateView):
    model = ContactPerson
    fields = ('first_name', 'last_name', 'contact_number', 'address')
    success_url = reverse_lazy('contacts:profile')
    template_name = 'contacts/create_contact.html'

    def form_valid(self, form):
        """
        Assign the newly created contact to the current logged in user.

        """

        form.instance.contact_owner = self.request.user
        return super(CreateContact, self).form_valid(form)


class UpdateContact(UpdateView):
    model = ContactPerson
    fields = ('first_name', 'last_name', 'contact_number', 'address')
    success_url = reverse_lazy('contacts:profile')
    template_name = 'contacts/update_contact.html'


class DeleteContact(DeleteView):
    model = ContactPerson
    context_object_name = 'contact'
    success_url = reverse_lazy('contacts:profile')
    template_name = 'contacts/delete_contact.html'
