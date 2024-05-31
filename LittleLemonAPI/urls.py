from django.urls import path
from . import views

urlpatterns = ('menu-items', views.MenuItemsView.as_view())
