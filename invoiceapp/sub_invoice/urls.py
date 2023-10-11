from django.urls import path
from .views import *


urlpatterns=[
   
    path("invoices",AllInvoices.as_view(),name="invoices"),
    path("invoices/new",AllInvoices.as_view(),name="newinvoices"),
    path("invoices/<int:id>",SingleInvoice.as_view(),name="singleInvoice"),
    path("invoices/<int:id>/items",AddItems.as_view(),name="AddItems"),
    path("user/signup/",SignupView.as_view(),name="SignupView"),
    path("user/login/",SigninView.as_view(),name="SigninView")
  
    ]