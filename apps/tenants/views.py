from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tenant
from .forms import TenantForm


# Create your views here.

class TenantListView(ListView):
    model = Tenant
    template_name = 'tenant_list.html'
    context_object_name = 'tenants'

class TenantDetailView(DetailView):
    model = Tenant
    template_name = 'tenant_detail.html'
    context_object_name = 'tenant'

class TenantCreateView(CreateView):
    model = Tenant
    template_name = 'add_tenant.html'
    form_class = TenantForm

    def get_success_url(self):
        return reverse_lazy('tenant_list')

class TenantUpdateView(UpdateView):
    model = Tenant
    template_name = 'edit_tenant.html'
    form_class = TenantForm

    def get_success_url(self):
        return reverse_lazy('tenant_list')

class TenantDeleteView(DeleteView):
    model = Tenant
    template_name = 'delete_tenant.html'
    success_url = reverse_lazy('tenant_list')


