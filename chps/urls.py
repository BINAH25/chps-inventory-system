from django.urls import path
from . import views

app_name = "chps"

urlpatterns = [
    path("", views.home, name="home"),
    path("send", views.send, name="send"),
    path("search", views.search, name="search"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete_patient/<int:pk>/", views.delete_patient, name="delete_patient"),
    path("patient_detail/<int:pk>/", views.patient_detail, name="patient_detail"),
    path("patients", views.patients, name="patients"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("log_out", views.log_out, name="log_out"),
    path("generate_pdf/<int:pk>/", views.generate_pdf, name="generate_pdf"),
]