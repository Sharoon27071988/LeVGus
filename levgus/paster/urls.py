from django.urls import path

from .views import HomeView, CategoryView, DecorativePlasterDetailView, CompanyInfoView, CooperatioInfo

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('decorativeplaster/<int:pk>/', DecorativePlasterDetailView.as_view(), name='decorative_plaster_detail'),
    path('company-info/', CompanyInfoView.as_view(), name='company_info'),
    path('cooperation-info/', CooperatioInfo.as_view(), name='cooperation_info')
]
