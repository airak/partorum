from django.contrib import admin
from django.urls import path

from . import views

app_name = 'clipping'

urlpatterns = [
	path('create_clipping/', views.ClippingCreate.as_view(), name='create_clipping'),
	path('update_clipping/<int:pk>/', views.ClippingUpdate.as_view(), name='update_clipping'),
	path('remove_clipping/<int:pk>/', views.ClippingDelete.as_view(), name='remove_clipping'),
	path('list_clipping/', views.ClippingListView.as_view(), name='list_clipping'),
]