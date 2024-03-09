from django.urls import path
from .views import TenantListView, TenantDetailView, TenantCreateView, TenantUpdateView, TenantDeleteView

urlpatterns = [
    path('tenants/', TenantListView.as_view(), name='tenant_list'),
    path('tenant/<int:pk>/', TenantDetailView.as_view(), name='tenant_detail'),
    path('tenant/add/', TenantCreateView.as_view(), name='add_tenant'),
    path('tenant/<int:pk>/edit/', TenantUpdateView.as_view(), name='edit_tenant'),
    path('tenant/<int:pk>/delete/', TenantDeleteView.as_view(), name='delete_tenant'),
]
