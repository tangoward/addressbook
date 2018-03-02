from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
import csv
from contacts.models import ContactPerson
from contacts.forms import UserCreateForm
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
        """
        List all the contacts associated to the currently logged in user.

        """

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
        return super().form_valid(form)


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


# CSV
class CsvView(TemplateView):
    success_url = reverse_lazy('contacts:profile')
    template_name = 'contacts/csv_read.html'

    def post(self, request, *args, **kwargs):

        new_csv = request.FILES['csv_file']

        with open(new_csv) as csvfile:
            readcsv = csv.reader(csvfile, delimiter=',')
            header = readcsv.next()

            for row in readcsv:
                new_contact = ContactPerson.objects.create(first_name=row[0], last_name=row[1], contact_number=row[2], address=row[3])

        return new_contact
