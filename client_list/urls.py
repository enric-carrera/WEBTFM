from django.urls import path
from . import views


urlpatterns = [

    path("clients_index/", views.clients_index, name="clients_index"),

    path("<int:pk>/", views.client_detail, name="client_detail"),

    path("add_client/", views.add_client, name="add_client"),

    path("eliminate_client/<int:pk>/", views.eliminate_client, name="eliminate_client"),
]
