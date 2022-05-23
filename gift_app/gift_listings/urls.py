from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gifts/entry', views.GiftCreateView.as_view(),name='gift_reg'),
    path('gifts/list/', views.GiftListView.as_view(),name='gift_list'),
    path('gifts/update/<int:pk>', views.GiftUpdateView.as_view,name='gift_update'),
]